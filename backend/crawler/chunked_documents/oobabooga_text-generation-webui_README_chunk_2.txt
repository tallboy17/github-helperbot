Repository: oobabooga/text-generation-webui
Language: Python
Stars: 44003
Forks: 5671
-----
- Supports multiple local text generation backends, including [llama.cpp](https://github.com/ggerganov/llama.cpp), [Transformers](https://github.com/huggingface/transformers), [ExLlamaV3](https://github.com/turboderp-org/exllamav3), [ExLlamaV2](https://github.com/turboderp-org/exllamav2), and [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) (the latter via its own [Dockerfile](https://github.com/oobabooga/text-generation-webui/blob/main/docker/TensorRT-LLM/Dockerfile)).
- Easy setup: Choose between **portable builds** (zero setup, just unzip and run) for GGUF models on Windows/Linux/macOS, or the one-click installer that creates a self-contained `installer_files` directory.
- 100% offline and private, with zero telemetry, external resources, or remote update requests.
- **File attachments**: Upload text files, PDF documents, and .docx documents to talk about their contents.
- **Web search**: Optionally search the internet with LLM-generated queries to add context to the conversation.
- Aesthetic UI with dark and light themes.
- `instruct` mode for instruction-following (like ChatGPT), and `chat-instruct`/`chat` modes for talking to custom characters.
- Automatic prompt formatting using Jinja2 templates. You don't need to ever worry about prompt formats.
- Edit messages, navigate between message versions, and branch conversations at any point.
- Multiple sampling parameters and generation options for sophisticated text generation control.
- Switch between different models in the UI without restarting.
- Automatic GPU layers for GGUF models (on NVIDIA GPUs).
- Free-form text generation in the Notebook tab without being limited to chat turns.
- OpenAI-compatible API with Chat and Completions endpoints, including tool-calling support – see [examples](https://github.com/oobabooga/text-generation-webui/wiki/12-%E2%80%90-OpenAI-API#examples).
- Extension support, with numerous built-in and user-contributed extensions available. See the [wiki](https://github.com/oobabooga/text-generation-webui/wiki/07-%E2%80%90-Extensions) and [extensions directory](https://github.com/oobabooga/text-generation-webui-extensions) for details.