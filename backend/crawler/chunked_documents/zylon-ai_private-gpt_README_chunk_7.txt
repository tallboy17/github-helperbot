Repository: zylon-ai/private-gpt
Language: Python
Stars: 56064
Forks: 7508
-----
Conceptually, PrivateGPT is an API that wraps a RAG pipeline and exposes its
primitives.
* The API is built using [FastAPI](https://fastapi.tiangolo.com/) and follows
[OpenAI's API scheme](https://platform.openai.com/docs/api-reference).
* The RAG pipeline is based on [LlamaIndex](https://www.llamaindex.ai/).  
The design of PrivateGPT allows to easily extend and adapt both the API and the
RAG implementation. Some key architectural decisions are:
* Dependency Injection, decoupling the different components and layers.
* Usage of LlamaIndex abstractions such as `LLM`, `BaseEmbedding` or `VectorStore`,
making it immediate to change the actual implementations of those abstractions.
* Simplicity, adding as few layers and new abstractions as possible.
* Ready to use, providing a full implementation of the API and RAG
pipeline.  
Main building blocks:
* APIs are defined in `private_gpt:server:<api>`. Each package contains an
`<api>_router.py` (FastAPI layer) and an `<api>_service.py` (the
service implementation). Each *Service* uses LlamaIndex base abstractions instead
of specific implementations,
decoupling the actual implementation from its usage.
* Components are placed in
`private_gpt:components:<component>`. Each *Component* is in charge of providing
actual implementations to the base abstractions used in the Services - for example
`LLMComponent` is in charge of providing an actual implementation of an `LLM`
(for example `LlamaCPP` or `OpenAI`).