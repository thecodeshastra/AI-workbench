"""File write tool for AI agent"""

# python module
import os
from typing import Dict, Any

# interface module
from interfaces.base_tool import BaseTool

# core module
from core.utils.logger import logger


class FileWriteTool(BaseTool):
    """
    Tool to write text content to a file.

    Args:
        BaseTool (BaseTool): Base tool class.
    """

    name = "file_write"

    def run(self, input: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run the tool.

        Args:
            input (Dict[str, Any]): Input parameters.
            context (Dict[str, Any]): Shared mutable state.

        Raises:
            RuntimeError: If run() is called instead of arun().
        """
        raise RuntimeError("FileWriteTool.run() should not be used. Use arun().")

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
            ValueError: If 'path' or 'source' is not provided in input.
            ValueError: If no content is found in context under 'source'.
        """
        path = input.get("path")
        source_key = input.get("source")

        if not path or not source_key:
            raise ValueError("file_write requires 'path' and 'source' in input")

        content = await context.get(source_key)
        if not content:
            raise ValueError(f"No content found in context under '{source_key}'")

        logger.info(f"Writing '{source_key}' to file: {path}")

        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        logger.info("File write successful")

        return {
            "status": "success",
            "path": path,
            "written_chars": len(content),
        }
