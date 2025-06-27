Repository: binary-husky/gpt_academic
Language: Python
Stars: 68796
Forks: 8352
-----
0. 部署项目的全部能力（这个是包含cuda和latex的大型镜像。但如果您网速慢、硬盘小，则不推荐该方法部署完整项目）
[![fullcapacity](https://github.com/binary-husky/gpt_academic/actions/workflows/build-with-all-capacity.yml/badge.svg?branch=master)](https://github.com/binary-husky/gpt_academic/actions/workflows/build-with-all-capacity.yml)  
``` sh
# 修改docker-compose.yml，保留方案0并删除其他方案。然后运行：
docker-compose up
```  
1. 仅ChatGPT + GLM4 + 文心一言+spark等在线模型（推荐大多数人选择）
[![basic](https://github.com/binary-husky/gpt_academic/actions/workflows/build-without-local-llms.yml/badge.svg?branch=master)](https://github.com/binary-husky/gpt_academic/actions/workflows/build-without-local-llms.yml)
[![basiclatex](https://github.com/binary-husky/gpt_academic/actions/workflows/build-with-latex.yml/badge.svg?branch=master)](https://github.com/binary-husky/gpt_academic/actions/workflows/build-with-latex.yml)
[![basicaudio](https://github.com/binary-husky/gpt_academic/actions/workflows/build-with-audio-assistant.yml/badge.svg?branch=master)](https://github.com/binary-husky/gpt_academic/actions/workflows/build-with-audio-assistant.yml)  
``` sh
# 修改docker-compose.yml，保留方案1并删除其他方案。然后运行：
docker-compose up
```  
P.S. 如果需要依赖Latex的插件功能，请见Wiki。另外，您也可以直接使用方案4或者方案0获取Latex功能。  
2. ChatGPT + GLM3 + MOSS + LLAMA2 + 通义千问（需要熟悉[Nvidia Docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#installing-on-ubuntu-and-debian)运行时）
[![chatglm](https://github.com/binary-husky/gpt_academic/actions/workflows/build-with-chatglm.yml/badge.svg?branch=master)](https://github.com/binary-husky/gpt_academic/actions/workflows/build-with-chatglm.yml)  
``` sh
# 修改docker-compose.yml，保留方案2并删除其他方案。然后运行：
docker-compose up
```