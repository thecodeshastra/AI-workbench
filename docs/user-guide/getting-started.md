# Getting Started

This guide will help you get up and running with the **AI-workbench**.

## Prerequisites

- Python 3.8 or higher
- `pip` (Python package installer)
- Access to a supported LLM provider (e.g., Gemini, OpenAI) - *Check `src/config/settings.py` for configuration details.*

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd AI-workbench
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration:**
   Create a `.env` file in the root directory and add your API keys.
   ```env
   # Example .env
   GOOGLE_API_KEY=your_api_key_here
   ```

5. **Currently supported Providers:**
   - Google Gemini
   - OpenAI
   - Claude (Anthropic)
   - Ollama
   - HuggingFace
   - Perplexity
   - LiteLLM (Generic all providers)

6. **Configuration:**
   - Edit `src/config/settings.py` to configure the LLM provider and other settings.
   - Settings like.
      - `MODEL_NAME`
      - `PROVIDER`
      - `TEMPERATURE`
      - `MAX_TOKENS`
      - `TIMEOUT_SECONDS`
      - `MAX_RETRIES`
      - `RETRY_BACKOFF`
      - etc...

## Basic Usage

### Running the Stateless Agent
The stateless agent is perfect for quick, single-turn interactions.

```bash
python src/run_stateless_agent.py
```

### Running the Summarizer Agent
The summarizer agent is designed for more complex tasks requiring planning and valid file operations.

```bash
python src/run_summarize_agent.py
```
