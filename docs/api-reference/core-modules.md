# Core Modules API Reference

## Provider Factory

::: src.core.provider_factory
    options:
      show_root_heading: true
      show_source: true

## Base Provider Interface

::: src.interfaces.base_provider.BaseProvider
    options:
      show_root_heading: true
      show_source: true

## Supported Providers

::: src.core.providers.gemini.GeminiProvider
    options:
      show_root_heading: true
      show_source: true

::: src.core.providers.openai.OpenAIProvider
    options:
      show_root_heading: true
      show_source: true

::: src.core.providers.anthropic.AnthropicProvider
    options:
      show_root_heading: true
      show_source: true

::: src.core.providers.litellm.LiteLLMProvider
    options:
      show_root_heading: true
      show_source: true

::: src.core.providers.ollama.OllamaProvider
    options:
      show_root_heading: true
      show_source: true

::: src.core.providers.perplexity.PerplexityProvider
    options:
      show_root_heading: true
      show_source: true

::: src.core.providers.huggingface.HuggingFaceProvider
    options:
      show_root_heading: true
      show_source: true

::: src.core.providers.mock_provider.MockProvider
    options:
      show_root_heading: true
      show_source: true

## Core Tools

::: src.core.tools.file_write.FileWrite
    options:
      show_root_heading: true
      show_source: true

::: src.core.tools.text_summarizer.TextSummarizer
    options:
      show_root_heading: true
      show_source: true

::: src.core.tools.extract_action.ExtractAction
    options:
      show_root_heading: true
      show_source: true

## Prompt Modules

::: src.core.prompts.base_persona
    options:
      show_root_heading: true

::: src.core.prompts.text_summarizer
    options:
      show_root_heading: true

::: src.core.prompts.extract_action
    options:
      show_root_heading: true

## Utilities

::: src.core.utils.logger
    options:
      show_root_heading: true

::: src.core.utils.context
    options:
      show_root_heading: true
