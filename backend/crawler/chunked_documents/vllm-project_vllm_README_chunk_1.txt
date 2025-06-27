Repository: vllm-project/vllm
Language: Python
Stars: 50150
Forks: 8201
-----
<p align="center">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/vllm-project/vllm/main/docs/assets/logos/vllm-logo-text-dark.png">
<img alt="vLLM" src="https://raw.githubusercontent.com/vllm-project/vllm/main/docs/assets/logos/vllm-logo-text-light.png" width=55%>
</picture>
</p>  
<h3 align="center">
Easy, fast, and cheap LLM serving for everyone
</h3>  
<p align="center">
| <a href="https://docs.vllm.ai"><b>Documentation</b></a> | <a href="https://blog.vllm.ai/"><b>Blog</b></a> | <a href="https://arxiv.org/abs/2309.06180"><b>Paper</b></a> | <a href="https://x.com/vllm_project"><b>Twitter/X</b></a> | <a href="https://discuss.vllm.ai"><b>User Forum</b></a> | <a href="https://slack.vllm.ai"><b>Developer Slack</b></a> |
</p>  
---  
*Latest News* 🔥
- [2025/05] We hosted [NYC vLLM Meetup](https://lu.ma/c1rqyf1f)! Please find the meetup slides [here](https://docs.google.com/presentation/d/1_q_aW_ioMJWUImf1s1YM-ZhjXz8cUeL0IJvaquOYBeA/edit?usp=sharing).
- [2025/05] vLLM is now a hosted project under PyTorch Foundation! Please find the announcement [here](https://pytorch.org/blog/pytorch-foundation-welcomes-vllm/).
- [2025/04] We hosted [Asia Developer Day](https://www.sginnovate.com/event/limited-availability-morning-evening-slots-remaining-inaugural-vllm-asia-developer-day)! Please find the meetup slides from the vLLM team [here](https://docs.google.com/presentation/d/19cp6Qu8u48ihB91A064XfaXruNYiBOUKrBxAmDOllOo/edit?usp=sharing).
- [2025/01] We are excited to announce the alpha release of vLLM V1: A major architectural upgrade with 1.7x speedup! Clean code, optimized execution loop, zero-overhead prefix caching, enhanced multimodal support, and more. Please check out our blog post [here](https://blog.vllm.ai/2025/01/27/v1-alpha-release.html).  
<details>
<summary>Previous News</summary>  
- [2025/03] We hosted [vLLM x Ollama Inference Night](https://lu.ma/vllm-ollama)! Please find the meetup slides from the vLLM team [here](https://docs.google.com/presentation/d/16T2PDD1YwRnZ4Tu8Q5r6n53c5Lr5c73UV9Vd2_eBo4U/edit?usp=sharing).
- [2025/03] We hosted [the first vLLM China Meetup](https://mp.weixin.qq.com/s/n77GibL2corAtQHtVEAzfg)! Please find the meetup slides from vLLM team [here](https://docs.google.com/presentation/d/1REHvfQMKGnvz6p3Fd23HhSO4c8j5WPGZV0bKYLwnHyQ/edit?usp=sharing).
- [2025/03] We hosted [the East Coast vLLM Meetup](https://lu.ma/7mu4k4xx)! Please find the meetup slides [here](https://docs.google.com/presentation/d/1NHiv8EUFF1NLd3fEYODm56nDmL26lEeXCaDgyDlTsRs/edit#slide=id.g31441846c39_0_0).
- [2025/02] We hosted [the ninth vLLM meetup](https://lu.ma/h7g3kuj9) with Meta! Please find the meetup slides from vLLM team [here](https://docs.google.com/presentation/d/1jzC_PZVXrVNSFVCW-V4cFXb6pn7zZ2CyP_Flwo05aqg/edit?usp=sharing) and AMD [here](https://drive.google.com/file/d/1Zk5qEJIkTmlQ2eQcXQZlljAx3m9s7nwn/view?usp=sharing). The slides from Meta will not be posted.
- [2025/01] We hosted [the eighth vLLM meetup](https://lu.ma/zep56hui) with Google Cloud! Please find the meetup slides from vLLM team [here](https://docs.google.com/presentation/d/1epVkt4Zu8Jz_S5OhEHPc798emsYh2BwYfRuDDVEF7u4/edit?usp=sharing), and Google Cloud team [here](https://drive.google.com/file/d/1h24pHewANyRL11xy5dXUbvRC9F9Kkjix/view?usp=sharing).
- [2024/12] vLLM joins [pytorch ecosystem](https://pytorch.org/blog/vllm-joins-pytorch)! Easy, Fast, and Cheap LLM Serving for Everyone!
- [2024/11] We hosted [the seventh vLLM meetup](https://lu.ma/h0qvrajz) with Snowflake! Please find the meetup slides from vLLM team [here](https://docs.google.com/presentation/d/1e3CxQBV3JsfGp30SwyvS3eM_tW-ghOhJ9PAJGK6KR54/edit?usp=sharing), and Snowflake team [here](https://docs.google.com/presentation/d/1qF3RkDAbOULwz9WK5TOltt2fE9t6uIc_hVNLFAaQX6A/edit?usp=sharing).
- [2024/10] We have just created a developer slack ([slack.vllm.ai](https://slack.vllm.ai)) focusing on coordinating contributions and discussing features. Please feel free to join us there!
- [2024/10] Ray Summit 2024 held a special track for vLLM! Please find the opening talk slides from the vLLM team [here](https://docs.google.com/presentation/d/1B_KQxpHBTRa_mDF-tR6i8rWdOU5QoTZNcEg2MKZxEHM/edit?usp=sharing). Learn more from the [talks](https://www.youtube.com/playlist?list=PLzTswPQNepXl6AQwifuwUImLPFRVpksjR) from other vLLM contributors and users!
- [2024/09] We hosted [the sixth vLLM meetup](https://lu.ma/87q3nvnh) with NVIDIA! Please find the meetup slides [here](https://docs.google.com/presentation/d/1wrLGwytQfaOTd5wCGSPNhoaW3nq0E-9wqyP7ny93xRs/edit?usp=sharing).
- [2024/07] We hosted [the fifth vLLM meetup](https://lu.ma/lp0gyjqr) with AWS! Please find the meetup slides [here](https://docs.google.com/presentation/d/1RgUD8aCfcHocghoP3zmXzck9vX3RCI9yfUAB2Bbcl4Y/edit?usp=sharing).
- [2024/07] In partnership with Meta, vLLM officially supports Llama 3.1 with FP8 quantization and pipeline parallelism! Please check out our blog post [here](https://blog.vllm.ai/2024/07/23/llama31.html).
- [2024/06] We hosted [the fourth vLLM meetup](https://lu.ma/agivllm) with Cloudflare and BentoML! Please find the meetup slides [here](https://docs.google.com/presentation/d/1iJ8o7V2bQEi0BFEljLTwc5G1S10_Rhv3beed5oB0NJ4/edit?usp=sharing).
- [2024/04] We hosted [the third vLLM meetup](https://robloxandvllmmeetup2024.splashthat.com/) with Roblox! Please find the meetup slides [here](https://docs.google.com/presentation/d/1A--47JAK4BJ39t954HyTkvtfwn0fkqtsL8NGFuslReM/edit?usp=sharing).
- [2024/01] We hosted [the second vLLM meetup](https://lu.ma/ygxbpzhl) with IBM! Please find the meetup slides [here](https://docs.google.com/presentation/d/12mI2sKABnUw5RBWXDYY-HtHth4iMSNcEoQ10jDQbxgA/edit?usp=sharing).
- [2023/10] We hosted [the first vLLM meetup](https://lu.ma/first-vllm-meetup) with a16z! Please find the meetup slides [here](https://docs.google.com/presentation/d/1QL-XPFXiFpDBh86DbEegFXBXFXjix4v032GhShbKf3s/edit?usp=sharing).
- [2023/08] We would like to express our sincere gratitude to [Andreessen Horowitz](https://a16z.com/2023/08/30/supporting-the-open-source-ai-community/) (a16z) for providing a generous grant to support the open-source development and research of vLLM.
- [2023/06] We officially released vLLM! FastChat-vLLM integration has powered [LMSYS Vicuna and Chatbot Arena](https://chat.lmsys.org) since mid-April. Check out our [blog post](https://vllm.ai).  
</details>  
---