"""Tool registry module for AI agent"""

# typing module
from typing import Dict

# core module
from core.tools.file_read import FileReadTool
from core.tools.text_summarizer import TextSummarizeTool
from core.tools.extract_action import ExtractActionsTool
from core.tools.file_write import FileWriteTool

# interfaces module
from interfaces.base_provider import BaseProvider


def build_tool_registry(provider: BaseProvider) -> Dict[str, object]:
    """
    Initialize all available tools.

    Args:
        provider (BaseProvider): The provider instance.

    Returns:
        Dict[str, object]: The tool registry.
    """
    return {
        "file_read": FileReadTool(),
        "text_summarize": TextSummarizeTool(provider),
        "extract_actions": ExtractActionsTool(provider),
        "file_write": FileWriteTool(),
    }
