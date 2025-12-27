"""Extract action tool for AI agent"""

# typing module
from typing import Dict, Any

# interface module
from interfaces.base_tool import BaseTool
from interfaces.base_provider import BaseProvider

# core module
from core.utils.logger import logger
from core.prompts.extract_action import ACTION_EXTRACTION_PROMPT
from core.prompts.base_persona import build_persona_system_prompt


class ExtractActionsTool(BaseTool):
    """
    Tool to extract action items from a summary.

    Args:
        BaseTool (BaseTool): Base tool class.
    """

    name = "extract_actions"
    description = "Extract action items from a summary."

    def __init__(self, provider: BaseProvider):
        """
        Initialize the ExtractActionsTool.

        Args:
            provider (BaseProvider): The provider instance.
        """
        self.provider = provider

    def run(self, input: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run the tool.

        Args:
            input (Dict[str, Any]): Input parameters.
            context (Dict[str, Any]): Shared mutable state.

        Raises:
            RuntimeError: If run() is called instead of arun().
        """
        raise RuntimeError("ExtractActionsTool.run() should not be used. Use arun().")

    async def arun(
        self, input: Dict[str, Any], context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Run the tool.

        Args:
            input (Dict[str, Any]): Input parameters.
            context (Dict[str, Any]): Shared mutable state.

        Returns:
            Dict[str, Any]: Result of the tool execution.
        """
        summary = await context.get("summary")
        if not summary:
            raise ValueError("extract_actions requires 'summary' in context")

        logger.info("Extracting action items from summary")

        final_prompt = f"""
{ACTION_EXTRACTION_PROMPT}

SUMMARY:
{summary}
"""

        system_prompt = build_persona_system_prompt("Expert action extractor")
        actions_text = await self.provider.generate_async(final_prompt, system_prompt)

        # Store for downstream tools
        await context.set("actions", actions_text)

        logger.info("Action extraction completed")

        return {
            "status": "success",
            "actions_length": len(actions_text),
        }
