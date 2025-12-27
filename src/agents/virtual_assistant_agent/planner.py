from core.prompts.base_persona import wrap_with_persona, build_persona_system_prompt
from .prompt import build_planner_prompt
from .common import extract_json


class Planner:
    def __init__(self, provider, memory_manager, tools_description: str):
        self.provider = provider
        self.memory = memory_manager
        self.tools_description = tools_description

    async def aplan(self, user_input: str, persona_context: str) -> dict:
        experience = self.memory.load_experience()
        relevant = [
            e["content"]
            for e in experience
            if any(word in e["content"].lower() for word in user_input.lower().split())
        ][:3]

        task_prompt = build_planner_prompt(
            user_input=user_input,
            tools_description=self.tools_description,
            experience_notes=relevant if relevant else None,
        )
        system_prompt = build_persona_system_prompt("Expert agent planner")
        final_prompt = wrap_with_persona(persona_context, task_prompt)
        response = await self.provider.generate_async(final_prompt, system_prompt)
        return extract_json(response)
