"""Planner class for the virtual assistant agent."""

# core module
from core.prompts.base_persona import wrap_with_persona, build_persona_system_prompt

# local module
from .prompt import build_planner_prompt
from .common import extract_json


class Planner:
    """Planner class for the virtual assistant agent."""

    def __init__(self, provider, memory_manager, tools_description: str) -> None:
        """Initializes the planner.

        Args:
            provider (BaseProvider): The provider.
            memory_manager (MemoryManager): The memory manager.
            tools_description (str): The tools description.
        """
        self.provider = provider
        self.memory = memory_manager
        self.tools_description = tools_description

    async def aplan(self, user_input: str, persona_context: str) -> dict:
        """Plans the user input.

        Args:
            user_input (str): The user input.
            persona_context (str): The persona context.

        Returns:
            dict: The plan.
        """
        experience = self.memory.load_experience()
        relevant = [
            e["content"]
            for e in experience
            if any(word in e["content"].lower() for word in user_input.lower().split())
        ][:3]

        task_prompt = build_planner_prompt(
            user_input=user_input,
            tools_description=self.tools_description,
            experience_notes=relevant if relevant else None,
        )
        system_prompt = build_persona_system_prompt("Expert agent planner")
        final_prompt = wrap_with_persona(persona_context, task_prompt)
        response = await self.provider.generate_async(final_prompt, system_prompt)
        return extract_json(response)
