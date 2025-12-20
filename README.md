# AI-workbench

A reusable library of AI agents for various automation tasks. This workbench includes stateless and stateful agents that can be used for code generation, text summarization, and multi-step task execution.

### [For Documentation Click Here](https://thecodeshastra.github.io/AI-workbench/)

## Features

- **Stateless Agent**: Lightweight, one-shot request/response agent for quick queries and code generation
- **Summarizer Agent**: Advanced planning and execution agent with async support for complex tasks
- **Multi-Provider Support**: Works with Gemini, OpenAI, Anthropic, LiteLLM, Ollama, Perplexity, HuggingFace, and more
- **Extensible Architecture**: Easy to add new agents and tools

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd AI-workbench
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file with your API keys:
   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage

### Stateless Agent
Run the stateless agent for quick, one-off requests:
```bash
python3 src/run_stateless_agent.py
```

### Summarizer Agent
Run the summarizer agent for planning and multi-step tasks:
```bash
python3 src/run_summarize_agent.py
```

## Documentation

This project uses **MkDocs** with the Dracula theme for documentation.

### View Documentation Locally
```bash
mkdocs serve
```
Then open http://127.0.0.1:8000 in your browser.

### Build Documentation
```bash
mkdocs build
```

### Deploy to GitHub Pages
```bash
mkdocs gh-deploy
```

### Quick MkDocs Notes
- Configuration: `mkdocs.yml`
- Documentation source: `docs/` folder
- User guides: `docs/user-guide/`
- API reference: `docs/api-reference/`
- Current theme: Dracula (dark mode)

## Project Structure

```
AI-workbench/
├── src/
│   ├── agents/           # Agent implementations
│   ├── core/            # Core modules (providers, tools, utils)
│   ├── config/          # Configuration settings
│   └── interfaces/      # Base interfaces
├── docs/                # MkDocs documentation
├── tests/               # Unit tests
└── requirements.txt     # Python dependencies
```

## License

See [LICENSE](LICENSE) file for details.
