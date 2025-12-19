"""Base tool interface for AI agent"""

# abc module
from abc import ABC, abstractmethod

# typing module
from typing import Dict, Any


class BaseTool(ABC):
    """
    Base interface for all tools.

    Args:
        ABC (ABC): Base class for abstract base classes.
    """

    name: str

    @abstractmethod
    def run(self, input: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the tool.

        input:
            Parameters provided by the planner for this step.

        context:
            Shared mutable state passed between steps.

        returns:
            A dictionary containing the result of the tool execution.
        """
        pass

    async def arun(
        self, input: Dict[str, Any], context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Async version (default: run sync in thread).
        Tools can override this.

        Args:
            input (Dict[str, Any]): Parameters provided by the planner for this step.
            context (Dict[str, Any]): Shared mutable state passed between steps.

        Returns:
            Dict[str, Any]: A dictionary containing the result of the tool execution.
        """
        return self.run(input, context)
