Repository: microsoft/autogen
Language: Python
Stars: 46193
Forks: 7005
-----
<div align="center">
<img src="autogen-landing.jpg" alt="AutoGen Landing" width="500">
</div>  
The AutoGen ecosystem provides everything you need to create AI agents, especially multi-agent workflows -- framework, developer tools, and applications.  
The _framework_ uses a layered and extensible design. Layers have clearly divided responsibilities and build on top of layers below. This design enables you to use the framework at different levels of abstraction, from high-level APIs to low-level components.  
- [Core API](./python/packages/autogen-core/) implements message passing, event-driven agents, and local and distributed runtime for flexibility and power. It also support cross-language support for .NET and Python.
- [AgentChat API](./python/packages/autogen-agentchat/) implements a simpler but opinionatedAPI for rapid prototyping. This API is built on top of the Core API and is closest to what users of v0.2 are familiar with and supports common multi-agent patterns such as two-agent chat or group chats.
- [Extensions API](./python/packages/autogen-ext/) enables first- and third-party extensions continuously expanding framework capabilities. It support specific implementation of LLM clients (e.g., OpenAI, AzureOpenAI), and capabilities such as code execution.  
The ecosystem also supports two essential _developer tools_:  
<div align="center">
<img src="https://media.githubusercontent.com/media/microsoft/autogen/refs/heads/main/python/packages/autogen-studio/docs/ags_screen.png" alt="AutoGen Studio Screenshot" width="500">
</div>  
- [AutoGen Studio](./python/packages/autogen-studio/) provides a no-code GUI for building multi-agent applications.
- [AutoGen Bench](./python/packages/agbench/) provides a benchmarking suite for evaluating agent performance.  
You can use the AutoGen framework and developer tools to create applications for your domain. For example, [Magentic-One](./python/packages/magentic-one-cli/) is a state-of-the-art multi-agent team built using AgentChat API and Extensions API that can handle a variety of tasks that require web browsing, code execution, and file handling.  
With AutoGen you get to join and contribute to a thriving ecosystem. We host weekly office hours and talks with maintainers and community. We also have a [Discord server](https://aka.ms/autogen-discord) for real-time chat, GitHub Discussions for Q&A, and a blog for tutorials and updates.