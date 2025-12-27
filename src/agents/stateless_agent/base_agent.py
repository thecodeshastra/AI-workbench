"""Agent that generates Python code based on user requests."""

# interface module
from interfaces.base_provider import BaseProvider

# core module
from core.utils.logger import logger
from core.prompts.base_prompt import build_persona_system_prompt

# stateless agent module
from .prompt import AGENT_PROMPT


class StatelessAgent:
    """
    Stateless AI agent that uses a provider to generate responses.
    """

    def __init__(self, provider: BaseProvider):
        """
        Initialize the agent with a provider.

        Args:
            provider (BaseProvider): The provider to use for generating responses.
        """
        self.provider = provider

    def _build_prompt(self, user_input: str) -> str:
        """
        Build the final prompt by combining agent instructions
        with the user request.

        Args:
            user_input (str): The user's input request.

        Returns:
            str: The final prompt.
        """
        return f"""{AGENT_PROMPT}

USER REQUEST:
{user_input}
"""

    def run(self, user_input: str) -> str:
        """
        Run the agent to generate a response.

        Args:
            user_input (str): The user's input request.

        Returns:
            str: The generated response.
        """
        logger.info("Agent run started")
        logger.info(f"User input length: {len(user_input)}")

        prompt = self._build_prompt(user_input)
        system_prompt = build_persona_system_prompt("stateless_agent")
        logger.info(f"Prompt length: {len(prompt)}")

        output = self.provider.generate(prompt, system_prompt)

        logger.info(f"Output length: {len(output)}")
        logger.info("Agent run finished")

        return output
