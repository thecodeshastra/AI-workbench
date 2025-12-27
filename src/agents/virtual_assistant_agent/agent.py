"""Virtual assistant agent"""

# asyncio module
import asyncio

# core module
from core.prompts.base_persona import build_persona_system_prompt, wrap_with_persona


class VirtualAssistantAgent:
    """Virtual assistant agent"""

    def __init__(self, persona_loader, planner, executor, provider, critic):
        """Initializes the virtual assistant agent.

        Args:
            persona_loader (PersonaLoader): The persona loader.
            planner (Planner): The planner.
            executor (Executor): The executor.
            provider (Provider): The provider.
            critic (Critic): The critic.
        """
        self.persona_context = persona_loader.load()
        self.planner = planner
        self.executor = executor
        self.provider = provider
        self.critic = critic

    async def arun(self, user_input: str):
        """Runs the virtual assistant agent.

        Args:
            user_input (str): The user input.

        Returns:
            str: The virtual assistant's response.
        """
        plan = await self.planner.aplan(
            user_input=user_input, persona_context=self.persona_context
        )

        # 🔹 CASE 1: Tool-based execution
        if plan.get("steps"):
            result = await self.executor.arun(plan)

        # 🔹 CASE 2: Direct chat (NO tools)
        else:
            system_prompt = build_persona_system_prompt(self.persona_context)
            prompt = wrap_with_persona(
                self.persona_context, f"Answer the following user query:\n{user_input}"
            )
            result = await self.provider.generate_async(prompt, system_prompt)

        # 🔥 Critic always runs
        await self.critic.ahandle(user_input, result)

        return result

    def run(self, user_input: str):
        """Runs the virtual assistant agent.

        Args:
            user_input (str): The user input.

        Returns:
            str: The virtual assistant's response.
        """
        return asyncio.run(self.arun(user_input))
