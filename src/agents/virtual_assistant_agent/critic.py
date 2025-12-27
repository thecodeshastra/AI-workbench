"""Critic class for the virtual assistant agent."""

# core module
from core.prompts.base_persona import build_persona_system_prompt
from interfaces.base_provider import BaseProvider

# local module
from .common import extract_json
from .memory.memory_manager import MemoryManager


class Critic:
    """
    Evaluates agent output and decides what to store in memory.
    """

    def __init__(self, provider: BaseProvider, memory_manager: MemoryManager):
        """Initializes the critic.

        Args:
            provider (BaseProvider): The provider.
            memory_manager (MemoryManager): The memory manager.
        """
        self.provider = provider
        self.memory = memory_manager

    async def aevaluate(
        self, user_input: str, agent_output: dict, system_prompt: str
    ) -> dict:
        """
        Evaluates the agent output and returns a judgment dict.

        Args:
            user_input (str): The user input.
            agent_output (dict): The agent output.
            system_prompt (str): The system prompt.

        Returns:
            dict: Returns a judgment dict:
            {
            "failure": bool,
            "unknown": bool,
            "lesson": str | null,
            "unknown_question": str | null
            }
        """

        prompt = f"""
You are a strict evaluator of an AI assistant's response.

USER INPUT:
{user_input}

AGENT OUTPUT:
{agent_output}

Evaluate carefully and return VALID JSON ONLY.

Rules:
- failure = true if the agent produced an error, wrong answer, or incomplete result
- unknown = true if the agent lacked information about the person it represents
- lesson = a short improvement insight if something can be learned
- unknown_question = the missing question if unknown is true

OUTPUT FORMAT:
{{
  "failure": bool,
  "unknown": bool,
  "lesson": str | null,
  "unknown_question": str | null
}}
"""
        response = await self.provider.generate_async(prompt, system_prompt)
        return extract_json(response)

    async def ahandle(self, user_input: str, agent_output: dict) -> None:
        """
        Handles the agent output.

        Args:
            user_input (str): The user input.
            agent_output (dict): The agent output.
        """
        system_prompt = build_persona_system_prompt("Expert critic")
        judgment = await self.aevaluate(user_input, agent_output, system_prompt)

        if judgment.get("failure"):
            self.memory.add_experience(
                content=judgment.get("lesson") or "Agent failure occurred",
                category="failure",
            )

        if judgment.get("lesson"):
            self.memory.add_experience(content=judgment["lesson"], category="lesson")

        if judgment.get("unknown") and judgment.get("unknown_question"):
            self.memory.add_unknown(judgment["unknown_question"])
