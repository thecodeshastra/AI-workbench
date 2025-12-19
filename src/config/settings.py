"""global settings module for AI agent"""

# # mocking the stateless agent
# PROVIDER = "mock"

# # ollama provider
# PROVIDER = "ollama"
# MODEL_NAME = "llama3.1:8b"

# # gemini provider
# PROVIDER = "gemini"
# MODEL_NAME = "gemini-2.5-flash"

# litellm provider
PROVIDER = "litellm"
MODEL_NAME = "gemini/gemini-2.5-flash"
LITELLM_MAX_TOKENS = 2048

# other settings
TEMPERATURE = 0.2
MAX_TOKENS = 500
TIMEOUT_SECONDS = 30
MAX_RETRIES = 3
RETRY_BACKOFF = 2
