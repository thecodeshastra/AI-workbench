def select_relevant_experience(
    experience: list[dict], user_input: str, max_items: int = 3
):
    """
    Select relevant experience entries using keyword matching.
    No summarization. No LLM. No token waste.
    """
    keywords = user_input.lower().split()

    relevant = []
    for entry in experience:
        text = entry.get("content", "").lower()
        if any(k in text for k in keywords):
            relevant.append(entry)

    return relevant[:max_items]
