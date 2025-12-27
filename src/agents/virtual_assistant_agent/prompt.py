def build_planner_prompt(
    user_input: str, tools_description: str, experience_notes: list[str] | None = None
) -> str:
    memory_block = ""
    if experience_notes:
        memory_block = "\nRELEVANT EXPERIENCE:\n" + "\n".join(
            f"- {note}" for note in experience_notes
        )

    return f"""
OBJECTIVE:
Convert the user request into a step-by-step execution plan.

AVAILABLE TOOLS:
{tools_description}
{memory_block}

USER REQUEST:
{user_input}

RULES:
- Use only listed tools
- Output VALID JSON ONLY
- Output format MUST NOT change

OUTPUT FORMAT:
{{
  "steps": []
}}
"""
