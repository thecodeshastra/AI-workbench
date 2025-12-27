"""Virtual Assistant Chatbot"""

import sys
import os

# Add the 'src' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# gradio module
import gradio as gr

# agent module
from agents.virtual_assistant_agent.agent import VirtualAssistantAgent
from agents.virtual_assistant_agent.persona_loader import PersonaLoader
from agents.virtual_assistant_agent.planner import Planner
from agents.virtual_assistant_agent.executor import Executor
from agents.virtual_assistant_agent.critic import Critic
from agents.virtual_assistant_agent.memory.memory_manager import MemoryManager
from agents.virtual_assistant_agent.constants import MEMORY_PATH, PERSONA_PATH

# core module
from core.provider_factory import get_provider
from core.tools.tool_registry import build_tool_registry

# ---------- Build Agent Once ----------


def build_agent():
    """Builds the virtual assistant agent."""

    persona_loader = PersonaLoader(PERSONA_PATH)

    memory_manager = MemoryManager(MEMORY_PATH)

    provider = get_provider()
    tools = build_tool_registry(provider)
    executor = Executor(tools)

    planner = Planner(
        provider=provider,
        memory_manager=memory_manager,
        tools_description=executor.describe_tools(),
    )

    critic = Critic(provider=provider, memory_manager=memory_manager)

    return VirtualAssistantAgent(
        persona_loader=persona_loader,
        provider=provider,
        planner=planner,
        executor=executor,
        critic=critic,
    )


agent = build_agent()


# ---------- Chat Function ----------


def chat_fn(message: str, history: list) -> str:
    """Chat function for the virtual assistant agent.

    Args:
        message (str): The user's message.
        history (list): The conversation history.

    Returns:
        str: The virtual assistant's response.
    """
    try:
        result = agent.run(message)

        # If tools produced a textual result, extract it
        if isinstance(result, dict):
            return result.get("summary") or str(result)

        return str(result)

    except Exception as e:
        return f"⚠️ Error: {str(e)}"


# ---------- Gradio UI ----------

demo = gr.ChatInterface(
    fn=chat_fn,
    title="Virtual Assistant (Persona-Based AI Agent)",
    description="An AI assistant that represents a real person, plans actions, uses tools, and learns over time.",
)

if __name__ == "__main__":
    demo.launch()
