"""Virtual assistance chatbot CLI interface"""

# agent module
from agents.virtual_assistant_agent.agent import VirtualAssistantAgent
from agents.virtual_assistant_agent.persona.persona_loader import PersonaLoader
from agents.virtual_assistant_agent.planner import Planner
from agents.virtual_assistant_agent.executor import Executor
from agents.virtual_assistant_agent.memory.memory_manager import MemoryManager
from agents.virtual_assistant_agent.constants import MEMORY_PATH, PERSONA_PATH

# core module
from core.provider_factory import get_provider
from core.tools.tool_registry import build_tool_registry


def main():
    """Main function for the virtual assistant agent."""
    persona_loader = PersonaLoader(PERSONA_PATH)

    memory_manager = MemoryManager(MEMORY_PATH)

    provider = get_provider()
    tools = build_tool_registry()
    executor = Executor(tools)

    planner = Planner(
        provider=provider,
        memory_manager=memory_manager,
        tools_description=executor.describe_tools(),
    )

    agent = VirtualAssistantAgent(
        persona_loader=persona_loader,
        planner=planner,
        executor=executor,
    )

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in {"exit", "quit"}:
            break

        result = agent.run(user_input)
        print("\nAgent Output:\n", result)


if __name__ == "__main__":
    main()
