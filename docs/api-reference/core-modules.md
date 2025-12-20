# Core Modules API Reference

## config

### Settings
::: src.config.settings.Settings
    options:
      show_root_heading: true
      show_source: true

## Provider Factory

The provider factory is responsible for initializing the appropriate LLM provider based on configuration settings.

::: src.core.provider_factory.get_provider
    options:
      show_root_heading: true
      show_source: true

## Base Provider Interface

All LLM providers implement this base interface:

::: src.interfaces.base_provider.BaseProvider
    options:
      show_root_heading: true
      show_source: true

## Supported Providers

The workbench supports multiple LLM providers:

### Gemini Provider
::: src.core.providers.gemini.GeminiProvider
    options:
      show_root_heading: true
      show_source: true

### OpenAI Provider
::: src.core.providers.openai.OpenAIProvider
    options:
      show_root_heading: true
      show_source: true

### Anthropic Provider
::: src.core.providers.anthropic.AnthropicProvider
    options:
      show_root_heading: true
      show_source: true

### LiteLLM Provider
::: src.core.providers.litellm.LiteLLMProvider
    options:
      show_root_heading: true
      show_source: true

### Ollama Provider
::: src.core.providers.ollama.OllamaProvider
    options:
      show_root_heading: true
      show_source: true

### Perplexity Provider
::: src.core.providers.perplexity.PerplexityProvider
    options:
      show_root_heading: true
      show_source: true

### HuggingFace Provider
::: src.core.providers.huggingface.HuggingFaceProvider
    options:
      show_root_heading: true
      show_source: true

### Mock Provider
::: src.core.providers.mock_provider.MockProvider
    options:
      show_root_heading: true
      show_source: true

## Core Tools

### BaseTool
::: src.core.tools.base_tool.BaseTool
    options:
      show_root_heading: true
      show_source: true

### File Read
::: src.core.tools.file_read.FileRead
    options:
      show_root_heading: true
      show_source: true

### File Write
::: src.core.tools.file_write.FileWrite
    options:
      show_root_heading: true
      show_source: true

### Text Summarizer
::: src.core.tools.text_summarizer.TextSummarizer
    options:
      show_root_heading: true
      show_source: true

### Extract Action Items
::: src.core.tools.extract_action_items.ExtractActionItems
    options:
      show_root_heading: true
      show_source: true

## Prompts

### Text Summarizer Prompt
::: src.core.prompts.text_summarizer.SUMMARIZER_PROMPT
    options:
      show_root_heading: true
      show_source: true

### Extract Action Prompt
::: src.core.prompts.extract_action.EXTRACT_ACTION_PROMPT
    options:
      show_root_heading: true
      show_source: true
