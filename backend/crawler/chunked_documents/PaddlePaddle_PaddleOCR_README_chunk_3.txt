Repository: PaddlePaddle/PaddleOCR
Language: Python
Stars: 50687
Forks: 8353
-----
🔥🔥2025.06.19: **PaddleOCR 3.0.2** 发布，包含：  
- **功能新增：**
- 模型默认下载源从`BOS`改为`HuggingFace`，同时也支持用户通过更改环境变量`PADDLE_PDX_MODEL_SOURCE`为`BOS`，将模型下载源设置为百度云对象存储BOS。
- PP-OCRv5、PP-StructureV3、PP-ChatOCRv4等pipeline新增C++、Java、Go、C#、Node.js、PHP 6种语言的服务调用示例。
- 优化PP-StructureV3产线中版面分区排序算法，对复杂竖版版面排序逻辑进行完善，进一步提升了复杂版面排序效果。
- 优化模型选择逻辑，当指定语言、未指定模型版本时，自动选择支持该语言的最新版本的模型。
-  为MKL-DNN缓存大小设置默认上界，防止缓存无限增长。同时，支持用户配置缓存容量。
- 更新高性能推理默认配置，支持Paddle MKL-DNN加速。优化高性能推理自动配置逻辑，支持更智能的配置选择。
- 调整默认设备获取逻辑，考虑环境中安装的Paddle框架对计算设备的实际支持情况，使程序行为更符合直觉。
- 新增PP-OCRv5的Android端示例，[详情](https://paddlepaddle.github.io/PaddleOCR/latest/version3.x/deployment/on_device_deployment.html)。  
- **Bug修复：**
- 修复PP-StructureV3部分CLI参数不生效的问题。
- 修复部分情况下`export_paddlex_config_to_yaml`无法正常工作的问题。
- 修复save_path实际行为与文档描述不符的问题。
- 修复基础服务化部署在使用MKL-DNN时可能出现的多线程错误。
- 修复Latex-OCR模型的图像预处理的通道顺序错误。
- 修复文本识别模块保存可视化图像的通道顺序错误。
- 修复PP-StructureV3中表格可视化结果通道顺序错误。
- 修复PP-StructureV3产线中极特殊的情况下，计算overlap_ratio时，变量溢出问题。  
- **文档优化：**
- 更新文档中对`enable_mkldnn`参数的说明，使其更准确地描述程序的实际行为。
- 修复文档中对`lang`和`ocr_version`参数描述的错误。
- 补充通过CLI导出产线配置文件的说明。
- 修复PP-OCRv5性能数据表格中的列缺失问题。
- 润色PP-StructureV3在不同配置下的benchmark指标。  
- **其他：**
- 放松numpy、pandas等依赖的版本限制，恢复对Python 3.12的支持。  
<details>
<summary><strong>历史日志</strong></summary>  
🔥🔥2025.06.05: **PaddleOCR 3.0.1** 发布，包含：  
- **优化部分模型和模型配置：**
- 更新 PP-OCRv5默认模型配置，检测和识别均由mobile改为server模型。为了改善大多数的场景默认效果，配置中的参数`limit_side_len`由736改为64
- 新增文本行方向分类`PP-LCNet_x1_0_textline_ori`模型，精度99.42%，OCR、PP-StructureV3、PP-ChatOCRv4产线的默认文本行方向分类器改为该模型
- 优化文本行方向分类`PP-LCNet_x0_25_textline_ori`模型，精度提升3.3个百分点，当前精度98.85%
- **优化和修复3.0.0版本部分存在的问题，[详情](https://paddlepaddle.github.io/PaddleOCR/latest/update/update.html)**  
🔥🔥2025.05.20: **PaddleOCR 3.0** 正式发布，包含：
- **PP-OCRv5**: 全场景高精度文字识别  
1. 🌐 单模型支持**五种**文字类型(**简体中文**、**繁体中文**、**中文拼音**、**英文**和**日文**)。
2. ✍️ 支持复杂**手写体**识别：复杂连笔、非规范字迹识别性能显著提升。
3. 🎯 整体识别精度提升 - 多种应用场景达到 SOTA 精度, 相比上一版本PP-OCRv4，识别精度**提升13个百分点**！  
- **PP-StructureV3**: 通用文档解析方案  
1. 🧮 支持多场景 PDF 高精度解析，在 OmniDocBench 基准测试中**领先众多开源和闭源方案**。
2. 🧠 多项专精能力: **印章识别**、**图表转表格**、**嵌套公式/图片的表格识别**、**竖排文本解析**及**复杂表格结构分析**等。  
- **PP-ChatOCRv4**: 智能文档理解方案
1. 🔥 文档图像（PDF/PNG/JPG）关键信息提取精度相比上一代**提升15个百分点**！
2. 💻 原生支持**文心大模型4.5 Turbo**，还兼容 PaddleNLP、Ollama、vLLM 等工具部署的大模型。
3. 🤝 集成 [PP-DocBee2](https://github.com/PaddlePaddle/PaddleMIX/tree/develop/paddlemix/examples/ppdocbee2)，支持印刷文字、手写体文字、印章信息、表格、图表等常见的复杂文档信息抽取和理解的能力。  
[更多日志](https://paddlepaddle.github.io/PaddleOCR/latest/update/update.html)  
</details>