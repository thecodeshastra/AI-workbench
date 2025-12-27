"""Planner module for AI agent"""

# python module
import json
from typing import Dict, Any

# interface module
from interfaces.base_provider import BaseProvider

# core module
from core.utils.logger import logger
from core.prompts.base_prompt import build_persona_system_prompt

# summarizer agent module
from agents.summarizer_agent.prompt import PLANNER_PROMPT


class Planner:
    """
    Planner converts a user request into a structured execution plan.
    """

    def __init__(self, provider: BaseProvider):
        """
        Initialize the planner.

        Args:
            provider (BaseProvider): The provider instance.
        """
        self.provider = provider

    def create_plan(self, user_request: str) -> Dict[str, Any]:
        """
        Create an execution plan based on the user request.

        Args:
            user_request (str): The user request.

        Returns:
            Dict[str, Any]: The execution plan.

        Raises:
            ValueError: If the plan is invalid.
        """
        logger.info("Planner started")

        prompt = f"""
{PLANNER_PROMPT}

USER REQUEST:
{user_request}
"""
        system_prompt = build_persona_system_prompt("Expert agent planner")
        raw_output = self.provider.generate(prompt, system_prompt)
        logger.info("Planner raw output received")
        cleaned_output = raw_output.strip()

        # Defensive cleanup for markdown fences
        if cleaned_output.startswith("```"):
            cleaned_output = cleaned_output.strip("`")
            cleaned_output = cleaned_output.replace("json", "", 1).strip()
        else:
            cleaned_output = raw_output.strip()

        try:
            plan = json.loads(cleaned_output)
        except json.JSONDecodeError as e:
            logger.error("Planner returned invalid JSON")
            logger.error(f"Raw output:\n{raw_output}")
            raise ValueError("Planner output is not valid JSON") from e

        self._validate_plan(plan)
        logger.info("Planner plan validated successfully")

        return plan

    def _validate_plan(self, plan: Dict[str, Any]) -> None:
        """
        Validate the execution plan.

        Args:
            plan (Dict[str, Any]): The execution plan.
        Raises:
            ValueError: If the plan is invalid.
        """
        if "steps" not in plan or not isinstance(plan["steps"], list):
            raise ValueError("Plan must contain a list of steps")

        for step in plan["steps"]:
            tool = step.get("tool")
            input_data = step.get("input")

            if not tool or not isinstance(input_data, dict):
                raise ValueError("Each step must have tool and input")

            if tool == "file_write":
                if "path" not in input_data or "source" not in input_data:
                    raise ValueError("file_write requires 'path' and 'source' in input")

            if "{{steps" in str(input_data):
                raise ValueError("Planner used forbidden step output references")
