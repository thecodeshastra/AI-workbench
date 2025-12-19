"""CLI entry point for the summarizer AI agent."""

# dotenv module
from dotenv import load_dotenv

# asyncio module
import asyncio

# core module
from core.utils.logger import logger
from core.provider_factory import get_provider

# summarizer agent module
from agents.summarizer_agent.planner import Planner
from agents.summarizer_agent.executor import Executor
from agents.summarizer_agent.async_executor import AsyncExecutor

load_dotenv()


def main():
    """
    Main function for running the summarizer agent.
    """
    print("Summarizer Automation Agent (v2)")
    print("--------------------------------")

    provider = get_provider()
    planner = Planner(provider)
    executor = Executor(provider)

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in {"exit", "quit"}:
            print("Exiting agent.")
            break

        try:
            # 1) Create execution plan
            plan = planner.create_plan(user_input)
            logger.info(f"Execution plan created: {plan}")

            # 2) Execute plan step-by-step with async executor
            # context = executor.run(plan)
            executor = AsyncExecutor(provider)
            context = asyncio.run(executor.run(plan))

            # 3) Present result
            print("\nAgent completed successfully.")
            if "summary" in context:
                print("\n--- SUMMARY ---\n")
                print(context["summary"])

            if "actions" in context:
                print("\n--- ACTION ITEMS ---\n")
                print(context["actions"])

        except Exception as e:
            logger.error(f"Agent failed: {e}")
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
