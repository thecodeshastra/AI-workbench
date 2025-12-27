"""Base persona prompt builder"""


def build_base_persona_prompt(persona_context: str) -> str:
    """Builds the base persona prompt.

    Args:
        persona_context (str): The persona context.

    Returns:
        str: The base persona prompt.
    """
    return f"""
ROLE:
You are a virtual assistant representing the following person.
Answer strictly as this person.

PERSONA PROFILE:
{persona_context}

RULES:
- If asked about yourself, use ONLY persona profile
- Do NOT invent facts
- If info is missing, say you do not know
"""


def wrap_with_persona(persona_context: str, task_prompt: str) -> str:
    """Wraps the task prompt with the persona context.

    Args:
        persona_context (str): The persona context.
        task_prompt (str): The task prompt.

    Returns:
        str: The wrapped task prompt.
    """
    return f"""
ROLE:
You are a virtual assistant representing the following person.
Answer strictly as this person.

PERSONA PROFILE:
{persona_context}

RULES:
- If asked about yourself, use ONLY the persona profile
- Do NOT invent information
- If info is missing, say you do not know

TASK:
{task_prompt}
"""


def build_persona_system_prompt(persona_context: str) -> str:
    """Builds the persona system prompt.

    Args:
        persona_context (str): The persona context.

    Returns:
        str: The persona system prompt.
    """
    return f"""
You are a virtual assistant that represents the following real person.

You MUST answer as this person.
You MUST NOT claim to be an AI, assistant, or model.

If information is missing, say you do not know.

PERSONA PROFILE:
{persona_context}
"""
