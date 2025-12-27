# Virtual Assistant Agent Guide

The **Virtual Assistant Agent** is a sophisticated, persona-based chatbot designed to represent a specific individual. it uses data from PDFs and text files to build its persona, maintains memory of interactions, and learns over time through a critic-led feedback loop.

## Key Features

- **Persona-Based**: Loads profile details from `profile.pdf` and `summary.txt` to act as a specific person.
- **Memory System**:
  - **Experiences**: Stores lessons, failures, and important insights from past interactions.
  - **Unknowns**: Automatically tracks questions it couldn't answer, allowing for manual updates to the persona.
- **Critic Loop**: A dedicated "Critic" evaluator analyzes every response to identify learning opportunities.
- **Gradio UI**: Comes with a built-in web interface for interactive chatting.

## How it Works

1.  **Persona Loading**: The agent reads files from the persona directory to understand its identity.
2.  **Planning**: For each user request, a `Planner` decides whether to use tools or respond directly using persona data.
3.  **Execution**: The `Executor` runs any planned tool steps.
4.  **Criticism & Learning**: After every response, the `Critic` evaluates the interaction and updates `experiences.json` or `unknowns.json`.

## Usage

To start the Virtual Assistant via the Gradio UI:

```bash
python3 src/apps/virtual_assistant_chatbot.py
```

This will launch a local web server (typically at http://127.0.0.1:7860) where you can chat with the assistant.

## Managing Memory

The agent's memory is stored in `src/agents/virtual_assistant_agent/memory/`:

- **`experience.json`**: contains history-based insights. This is automatically updated by the Critic.
- **`unknowns.json`**: Contains a list of questions the agent couldn't answer. 

> [!TIP]
> You can manually move items from `unknowns.json` to your persona files or `experience.json` to "teach" the agent new information about the persona.
