"""Provider factory module for AI agent"""

# stateless ai agent modules
from config.settings import (
    PROVIDER,
    MODEL_NAME,
    TEMPERATURE,
    MAX_TOKENS,
)

from providers.mock_provider import MockProvider
from providers.ollama import OllamaProvider
from providers.gemini import GeminiProvider
from providers.openai import OpenAIProvider
from providers.anthropic import AnthropicProvider
from providers.perplexity import PerplexityProvider
from providers.huggingface import HuggingFaceProvider

from core.utils.logger import logger


def get_provider():
    """Get provider based on the configuration.

    Returns:
        BaseProvider: The provider instance.

    Raises:
        ValueError: If the provider is unknown.
    """

    logger.info("Initializing provider: %s", PROVIDER)

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
