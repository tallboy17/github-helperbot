Repository: hpcaitech/ColossalAI
Language: Python
Stars: 40976
Forks: 4521
-----
This project is inspired by some related projects (some by our team and some by other organizations). We would like to credit these amazing projects as listed in the [Reference List](./docs/REFERENCE.md).  
To cite this project, you can use the following BibTeX citation.  
```
@inproceedings{10.1145/3605573.3605613,
author = {Li, Shenggui and Liu, Hongxin and Bian, Zhengda and Fang, Jiarui and Huang, Haichen and Liu, Yuliang and Wang, Boxiang and You, Yang},
title = {Colossal-AI: A Unified Deep Learning System For Large-Scale Parallel Training},
year = {2023},
isbn = {9798400708435},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3605573.3605613},
doi = {10.1145/3605573.3605613},
abstract = {The success of Transformer models has pushed the deep learning model scale to billions of parameters, but the memory limitation of a single GPU has led to an urgent need for training on multi-GPU clusters. However, the best practice for choosing the optimal parallel strategy is still lacking, as it requires domain expertise in both deep learning and parallel computing. The Colossal-AI system addressed the above challenge by introducing a unified interface to scale your sequential code of model training to distributed environments. It supports parallel training methods such as data, pipeline, tensor, and sequence parallelism and is integrated with heterogeneous training and zero redundancy optimizer. Compared to the baseline system, Colossal-AI can achieve up to 2.76 times training speedup on large-scale models.},
booktitle = {Proceedings of the 52nd International Conference on Parallel Processing},
pages = {766–775},
numpages = {10},
keywords = {datasets, gaze detection, text tagging, neural networks},
location = {Salt Lake City, UT, USA},
series = {ICPP '23}
}
```  
Colossal-AI has been accepted as official tutorial by top conferences [NeurIPS](https://nips.cc/), [SC](https://sc22.supercomputing.org/), [AAAI](https://aaai.org/Conferences/AAAI-23/),
[PPoPP](https://ppopp23.sigplan.org/), [CVPR](https://cvpr2023.thecvf.com/), [ISC](https://www.isc-hpc.com/), [NVIDIA GTC](https://www.nvidia.com/en-us/on-demand/session/gtcspring23-S51482/) ,etc.  
<p align="right">(<a href="#top">back to top</a>)</p>