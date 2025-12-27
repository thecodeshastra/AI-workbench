class Executor:
    def __init__(self, tool_registry: dict):
        self.tools = tool_registry
        self.context = {}

    async def arun(self, plan: dict):
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

    def describe_tools(self):
        return "\n".join(
            f"- {name}: {tool.description}" for name, tool in self.tools.items()
        )
