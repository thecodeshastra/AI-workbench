"""LiteLLM provider module for AI agent"""

# python module
import time
import asyncio
from typing import Optional

# litellm module
from litellm import completion, acompletion

# interface module
from interfaces.base_provider import BaseProvider

# core module
from core.utils.logger import logger


class LiteLLMProvider(BaseProvider):
    """
    Unified LLM provider using LiteLLM.
    Handles retries, timeouts, and logging.

    Args:
        BaseProvider (BaseProvider): Base provider class.
    """

    def __init__(
        self,
        model: str,
        temperature: float = 0.2,
        max_tokens: Optional[int] = None,
        timeout: int = 30,
        max_retries: int = 3,
        backoff: int = 2,
    ):
        """
        Initialize the LiteLLMProvider.

        Args:
            model (str): The model name.
            temperature (float, optional): The temperature for the model.
            max_tokens (Optional[int], optional): The maximum number of tokens.
            timeout (int, optional): The timeout in seconds.
            max_retries (int, optional): The maximum number of retries.
            backoff (int, optional): The backoff factor.
        """
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout
        self.max_retries = max_retries
        self.backoff = backoff

    def generate(self, prompt: str) -> str:
        """
        Generate a response using the LLM.

        Args:
            prompt (str): The input prompt.

        Returns:
            str: The generated response.
        Raises:
            RuntimeError: If the LLM call fails after retries.
        """
        for attempt in range(1, self.max_retries + 1):
            start = time.time()
            try:
                logger.info(f"LLM call (sync) | model={self.model} | attempt={attempt}")

                response = completion(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                    timeout=self.timeout,
                )

                latency = round(time.time() - start, 2)
                logger.info(f"LLM success | latency={latency}s")

                return response["choices"][0]["message"]["content"]

            except Exception as e:
                logger.warning(f"LLM failed (attempt {attempt}): {e}")

                if attempt == self.max_retries:
                    raise RuntimeError("LLM failed after retries") from e

                time.sleep(self.backoff**attempt)

    async def generate_async(self, prompt: str) -> str:
        """
        Generate a response using the LLM asynchronously.

        Args:
            prompt (str): The input prompt.

        Returns:
            str: The generated response.
        Raises:
            RuntimeError: If the LLM call fails after retries.
        """
        for attempt in range(1, self.max_retries + 1):
            start = time.time()
            try:
                logger.info(
                    f"LLM call (async) | model={self.model} | attempt={attempt}"
                )

                response = await acompletion(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                    timeout=self.timeout,
                )

                latency = round(time.time() - start, 2)
                logger.info(f"LLM success | latency={latency}s")

                return response["choices"][0]["message"]["content"]

            except Exception as e:
                logger.warning(f"LLM async failed (attempt {attempt}): {e}")

                if attempt == self.max_retries:
                    raise RuntimeError("LLM async failed after retries") from e

                await asyncio.sleep(self.backoff**attempt)
