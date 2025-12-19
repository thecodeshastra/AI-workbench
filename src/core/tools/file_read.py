"""File read tool for AI agent"""

# python module
import os
from typing import Dict, Any

# interface module
from interfaces.base_tool import BaseTool

# core module
from core.utils.logger import logger


class FileReadTool(BaseTool):
    """
    Tool to read text content from a file.

    Args:
        BaseTool (BaseTool): Base tool class.
    """

    name = "file_read"

    def run(self, input: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run the tool.

        Args:
            input (Dict[str, Any]): Input parameters.
            context (Dict[str, Any]): Shared mutable state.

        Raises:
            RuntimeError: If run() is called instead of arun().
        """
        raise RuntimeError("FileReadTool.run() should not be used. Use arun().")

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

        Raises:
            ValueError: If 'path' is not provided in input.
            FileNotFoundError: If the file does not exist.
        """
        path = input.get("path")
        if not path:
            raise ValueError("file_read requires 'path' in input")

        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")

        logger.info(f"Reading file: {path}")

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        # Store in context for downstream tools
        await context.set("text", text)

        logger.info(f"File read successful, length={len(text)}")

        return {
            "status": "success",
            "chars": len(text),
            "path": path,
        }
