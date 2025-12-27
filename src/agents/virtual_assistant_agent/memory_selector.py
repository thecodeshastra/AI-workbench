"""Memory selector class for the virtual assistant agent."""


def select_relevant_experience(
    experience: list[dict], user_input: str, max_items: int = 3
) -> list[dict]:
    """
    Select relevant experience entries using keyword matching.
    No summarization. No LLM. No token waste.

    Args:
        experience (list[dict]): The experience.
        user_input (str): The user input.
        max_items (int, optional): The maximum number of items. Defaults to 3.

    Returns:
        list[dict]: The relevant experience entries.
    """
    keywords = user_input.lower().split()

    relevant = []
    for entry in experience:
        text = entry.get("content", "").lower()
        if any(k in text for k in keywords):
            relevant.append(entry)

    return relevant[:max_items]
