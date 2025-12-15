"""CLI entry point for the stateless AI agent."""

# dotenv module
from dotenv import load_dotenv

# stateless agent module
from agents.stateless_agent.base_agent import StatelessAgent
from provider_factory import get_provider

load_dotenv()


def main():
    """Main function to run the stateless AI agent"""
    print("Stateless AI Agent (Multi-Provider)")
    print("----------------------------------")

    provider = get_provider()
    agent = StatelessAgent(provider)

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in {"exit", "quit"}:
            print("Exiting agent.")
            break

        output = agent.run(user_input)
        print("\nAgent:\n")
        print(output)


if __name__ == "__main__":
    main()
