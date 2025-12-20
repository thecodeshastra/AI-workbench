"""Async executor for Summarizer Agent"""

# Standard library imports
import uuid
import asyncio
from typing import Dict, Any

# core modules
from core.tools.tool_registry import build_tool_registry
from core.utils.logger import logger
from core.utils.context import AgentContext


class AsyncExecutor:
    """Async executor for Summarizer Agent"""

    def __init__(self, provider):
        """Initialize the async executor"""
        self.tools = build_tool_registry(provider)

    async def _run_tool(self, tool_name, input_data, context):
        """Run a tool

        Args:
            tool_name (str): Name of the tool to run
            input_data (Any): Input data for the tool
            context (AgentContext): Agent context

        Returns:
            Any: Result of the tool execution

        Raises:
            KeyError: If the tool is not found
        """
        step_id = str(uuid.uuid4())[:8]
        logger.info(f"[{step_id}] Starting tool: {tool_name}")
        result = await self.tools[tool_name].arun(input_data, context)
        logger.info(f"[{step_id}] Finished tool: {tool_name}")
        return result

    async def run(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        context = AgentContext()

        for step in plan["steps"]:
            if "parallel" in step:
                await asyncio.gather(
                    *[
                        self._run_tool(s["tool"], s["input"], context)
                        for s in step["parallel"]
                    ]
                )
            else:
                tool = self.tools[step["tool"]]
                await tool.arun(step["input"], context)

        return await context.snapshot()
