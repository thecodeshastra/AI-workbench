"""Provider factory module for AI agent"""

# config module
from config.settings import (
    PROVIDER,
    MODEL_NAME,
    TEMPERATURE,
    MAX_TOKENS,
    TIMEOUT_SECONDS,
    MAX_RETRIES,
    RETRY_BACKOFF,
    LITELLM_MAX_TOKENS,
)

# providers module
from core.providers.mock_provider import MockProvider
from core.providers.ollama import OllamaProvider
from core.providers.gemini import GeminiProvider
from core.providers.openai import OpenAIProvider
from core.providers.anthropic import AnthropicProvider
from core.providers.perplexity import PerplexityProvider
from core.providers.huggingface import HuggingFaceProvider
from core.providers.litellm import LiteLLMProvider

# core module
from core.utils.logger import logger


def get_provider():
    """Get provider based on the configuration.

    Returns:
        BaseProvider: The provider instance.

    Raises:
        ValueError: If the provider is unknown.
    """

    logger.info("Initializing provider: %s", PROVIDER)

    if PROVIDER == "litellm":
        return LiteLLMProvider(
            MODEL_NAME,
            TEMPERATURE,
            LITELLM_MAX_TOKENS,
            TIMEOUT_SECONDS,
            MAX_RETRIES,
            RETRY_BACKOFF,
        )

    if PROVIDER == "mock":
        return MockProvider()

    if PROVIDER == "ollama":
        return OllamaProvider(MODEL_NAME, TEMPERATURE)

    if PROVIDER == "gemini":
        return GeminiProvider(MODEL_NAME, TEMPERATURE)

    if PROVIDER == "openai":
        return OpenAIProvider(MODEL_NAME, TEMPERATURE, MAX_TOKENS)

    if PROVIDER == "anthropic":
        return AnthropicProvider(MODEL_NAME, TEMPERATURE, MAX_TOKENS)

    if PROVIDER == "perplexity":
        return PerplexityProvider(MODEL_NAME, TEMPERATURE)

    if PROVIDER == "huggingface":
        return HuggingFaceProvider(TEMPERATURE, MAX_TOKENS)

    raise ValueError(f"Unknown provider: {PROVIDER}")
