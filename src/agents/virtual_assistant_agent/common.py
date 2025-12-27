"""Common functions for the virtual assistant agent."""

# python modules
import json
import re


def extract_json(text: str) -> dict:
    """
    Extract JSON object from LLM output safely.

    Args:
        text (str): The text to extract JSON from.

    Returns:
        dict: The extracted JSON object.
    """
    if not text or not text.strip():
        raise ValueError("Planner returned empty response")

    # Remove markdown fences if present
    text = text.strip()
    text = re.sub(r"^```json", "", text)
    text = re.sub(r"```$", "", text)

    # Find first JSON object
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        raise ValueError(f"No JSON object found in planner output:\n{text}")

    return json.loads(match.group())
