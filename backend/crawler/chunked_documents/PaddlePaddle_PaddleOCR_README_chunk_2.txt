Repository: PaddlePaddle/PaddleOCR
Language: Python
Stars: 50687
Forks: 8353
-----
PaddleOCR自发布以来凭借学术前沿算法和产业落地实践，受到了产学研各方的喜爱，并被广泛应用于众多知名开源项目，例如：Umi-OCR、OmniParser、MinerU、RAGFlow等，已成为广大开发者心中的开源OCR领域的首选工具。2025年5月20日，飞桨团队发布**PaddleOCR 3.0**，全面适配**飞桨框架3.0正式版**，进一步**提升文字识别精度**，支持**多文字类型识别**和**手写体识别**，满足大模型应用对**复杂文档高精度解析**的旺盛需求，结合**文心大模型4.5 Turbo**显著提升关键信息抽取精度，并新增**对昆仑芯、昇腾等国产硬件**的支持。完整使用文档请参考 [PaddleOCR 3.0 文档](https://paddlepaddle.github.io/PaddleOCR/latest/)。  
PaddleOCR 3.0**新增**三大特色能力：
- 全场景文字识别模型[PP-OCRv5](docs/version3.x/algorithm/PP-OCRv5/PP-OCRv5.md)：单模型支持五种文字类型和复杂手写体识别；整体识别精度相比上一代**提升13个百分点**。[在线体验](https://aistudio.baidu.com/community/app/91660/webUI)
- 通用文档解析方案[PP-StructureV3](docs/version3.x/algorithm/PP-StructureV3/PP-StructureV3.md)：支持多场景、多版式 PDF 高精度解析，在公开评测集中**领先众多开源和闭源方案**。[在线体验](https://aistudio.baidu.com/community/app/518494/webUI)
- 智能文档理解方案[PP-ChatOCRv4](docs/version3.x/algorithm/PP-ChatOCRv4/PP-ChatOCRv4.md)：原生支持文心大模型4.5 Turbo，精度相比上一代**提升15个百分点**。[在线体验](https://aistudio.baidu.com/community/app/518493/webUI)  
PaddleOCR 3.0除了提供优秀的模型库外，还提供好学易用的工具，覆盖模型训练、推理和服务化部署，方便开发者快速落地AI应用。
<div align="center">
<p>
<img width="100%" src="./docs/images/Arch_cn.png" alt="PaddleOCR Architecture"></a>
</p>
</div>