"""Executor class for the virtual assistant agent."""


class Executor:
    """Executor class for the virtual assistant agent."""

    def __init__(self, tool_registry: dict):
        """Initializes the executor.

        Args:
            tool_registry (dict): The tool registry.
        """
        self.tools = tool_registry
        self.context = {}

    async def arun(self, plan: dict) -> dict:
        """Runs the executor.

        Args:
            plan (dict): The plan.

        Returns:
            dict: The context.
        """
        if "steps" not in plan:
            raise ValueError("Invalid plan format")

        for step in plan["steps"]:
            tool_name = step["tool"]
            tool_input = step.get("input", {})

            tool = self.tools.get(tool_name)
            if not tool:
                raise ValueError(f"Tool not found: {tool_name}")

            await tool.arun(self.context, **tool_input)

        return self.context

    def describe_tools(self) -> str:
        """Describes the tools.

        Returns:
            str: The tools description.
        """
        return "\n".join(
            f"- {name}: {tool.description}" for name, tool in self.tools.items()
        )
