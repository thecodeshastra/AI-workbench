"""Executor module for AI agent"""

# python module
from typing import Dict, Any

# interface module
from interfaces.base_provider import BaseProvider

# core module
from core.tools.tool_registry import build_tool_registry
from core.utils.logger import logger


class Executor:
    """
    Executes a validated multi-step plan using registered tools.
    """

    def __init__(self, provider: BaseProvider):
        """
        Initialize the executor.

        Args:
            provider (BaseProvider): The provider instance.
        """
        self.tools = build_tool_registry(provider)

    def run(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run the executor.

        Args:
            plan (Dict[str, Any]): The plan to run.

        Returns:
            Dict[str, Any]: The context.
        """
        context: Dict[str, Any] = {}

        logger.info("Executor started")

        for idx, step in enumerate(plan["steps"], start=1):
            tool_name = step["tool"]
            input_data = step["input"]

            logger.info(f"Executing step {idx}: {tool_name}")

            tool = self.tools.get(tool_name)
            if not tool:
                raise ValueError(f"Unknown tool: {tool_name}")

            result = tool.run(input_data, context)
            logger.info(f"Step {idx} completed: {result}")

        logger.info("Executor finished all steps")
        return context
