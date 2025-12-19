"""Text summarizer tool for AI agent"""

# typing module
from typing import Dict, Any

# interface module
from interfaces.base_tool import BaseTool
from interfaces.base_provider import BaseProvider

# core module
from core.utils.logger import logger
from core.prompts.text_summarizer import ADVANCED_SUMMARIZATION_PROMPT


class TextSummarizeTool(BaseTool):
    """
    Tool to summarize text using an LLM.

    Args:
        BaseTool (BaseTool): Base tool class.
    """

    name = "text_summarize"

    def __init__(self, provider: BaseProvider):
        """
        Initialize the TextSummarizeTool.

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
        raise RuntimeError("TextSummarizeTool.run() should not be used. Use arun().")

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
        source_text = await context.get("text")
        if not source_text:
            raise ValueError("text_summarize requires 'text' in context")

        logger.info("Running text summarization")

        final_prompt = f"""
{ADVANCED_SUMMARIZATION_PROMPT}

SOURCE CONTENT:
{source_text}
"""

        summary = await self.provider.generate_async(final_prompt)

        # Store for downstream tools
        await context.set("summary", summary)

        logger.info("Text summarization completed")

        return {
            "status": "success",
            "summary_length": len(summary),
        }
