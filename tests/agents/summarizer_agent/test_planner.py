"""
Test module for Planner in summarizer agent.

This module contains unit tests for the Planner class,
verifying plan creation and validation functionality.
"""

import unittest
from unittest.mock import Mock
from typing import Dict, Any

from src.agents.summarizer_agent.planner import Planner


class TestPlanner(unittest.TestCase):
    """
    Test cases for the Planner class.

    This class tests the planning capabilities of the summarizer agent,
    including plan generation and validation.
    """

    def setUp(self) -> None:
        """
        Set up test fixtures.

        Creates a mock provider and Planner instance.
        """
        self.provider: Mock = Mock()
        self.provider.generate.return_value = (
            '{"steps": [{"tool": "file_read", "input": {"path": "test.txt"}}]}'
        )
        self.planner: Planner = Planner(self.provider)

    def test_create_plan(self) -> None:
        """
        Test plan creation.

        Verifies that create_plan returns a valid plan dictionary.
        """
        plan: Dict[str, Any] = self.planner.create_plan("test")
        self.assertIn("steps", plan)
        self.assertEqual(len(plan["steps"]), 1)

    def test_validate_plan_valid(self) -> None:
        """
        Test validation of a valid plan.

        Ensures no exception is raised for a properly structured plan.
        """
        plan: Dict[str, Any] = {
            "steps": [{"tool": "file_read", "input": {"path": "test.txt"}}]
        }
        self.planner._validate_plan(plan)  # Should not raise

    def test_validate_plan_no_steps(self) -> None:
        """
        Test validation of plan without steps.

        Verifies that ValueError is raised for invalid plan structure.
        """
        plan: Dict[str, Any] = {}
        with self.assertRaises(ValueError):
            self.planner._validate_plan(plan)

    def test_validate_plan_invalid_step(self) -> None:
        """
        Test validation of plan with invalid step.

        Ensures ValueError is raised when step lacks required fields.
        """
        plan: Dict[str, Any] = {"steps": [{"tool": "file_read"}]}
        with self.assertRaises(ValueError):
            self.planner._validate_plan(plan)


if __name__ == "__main__":
    unittest.main()
