Repository: zylon-ai/private-gpt
Language: Python
Stars: 56064
Forks: 7508
-----
<a href="https://trendshift.io/repositories/2601" target="_blank"><img src="https://trendshift.io/api/badge/repositories/2601" alt="imartinez%2FprivateGPT | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>  
[![Tests](https://github.com/zylon-ai/private-gpt/actions/workflows/tests.yml/badge.svg)](https://github.com/zylon-ai/private-gpt/actions/workflows/tests.yml?query=branch%3Amain)
[![Website](https://img.shields.io/website?up_message=check%20it&down_message=down&url=https%3A%2F%2Fdocs.privategpt.dev%2F&label=Documentation)](https://docs.privategpt.dev/)
[![Discord](https://img.shields.io/discord/1164200432894234644?logo=discord&label=PrivateGPT)](https://discord.gg/bK6mRVpErU)
[![X (formerly Twitter) Follow](https://img.shields.io/twitter/follow/ZylonPrivateGPT)](https://twitter.com/ZylonPrivateGPT)  
![Gradio UI](/fern/docs/assets/ui.png?raw=true)  
PrivateGPT is a production-ready AI project that allows you to ask questions about your documents using the power
of Large Language Models (LLMs), even in scenarios without an Internet connection. 100% private, no data leaves your
execution environment at any point.  
>[!TIP]
> If you are looking for an **enterprise-ready, fully private AI workspace**
> check out [Zylon's website](https://zylon.ai)  or [request a demo](https://cal.com/zylon/demo?source=pgpt-readme).
> Crafted by the team behind PrivateGPT, Zylon is a best-in-class AI collaborative
> workspace that can be easily deployed on-premise (data center, bare metal...) or in your private cloud (AWS, GCP, Azure...).  
The project provides an API offering all the primitives required to build private, context-aware AI applications.
It follows and extends the [OpenAI API standard](https://openai.com/blog/openai-api),
and supports both normal and streaming responses.  
The API is divided into two logical blocks:  
**High-level API**, which abstracts all the complexity of a RAG (Retrieval Augmented Generation)
pipeline implementation:
- Ingestion of documents: internally managing document parsing,
splitting, metadata extraction, embedding generation and storage.
- Chat & Completions using context from ingested documents:
abstracting the retrieval of context, the prompt engineering and the response generation.  
**Low-level API**, which allows advanced users to implement their own complex pipelines:
- Embeddings generation: based on a piece of text.
- Contextual chunks retrieval: given a query, returns the most relevant chunks of text from the ingested documents.  
In addition to this, a working [Gradio UI](https://www.gradio.app/)
client is provided to test the API, together with a set of useful tools such as bulk model
download script, ingestion script, documents folder watch, etc.