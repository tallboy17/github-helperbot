Repository: hiyouga/LLaMA-Factory
Language: Python
Stars: 52604
Forks: 6439
-----
To enable FlashAttention-2 on the Windows platform, please use the script from [flash-attention-windows-wheel](https://huggingface.co/lldacing/flash-attention-windows-wheel) to compile and install it by yourself.  
</details>  
<details><summary>For Ascend NPU users</summary>  
To install LLaMA Factory on Ascend NPU devices, please upgrade Python to version 3.10 or higher and specify extra dependencies: `pip install -e ".[torch-npu,metrics]"`. Additionally, you need to install the **[Ascend CANN Toolkit and Kernels](https://www.hiascend.com/developer/download/community/result?module=cann)**. Please follow the [installation tutorial](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/600alphaX/softwareinstall/instg/atlasdeploy_03_0031.html) or use the following commands:  
```bash
# replace the url according to your CANN version and devices
# install CANN Toolkit
wget https://ascend-repo.obs.cn-east-2.myhuaweicloud.com/Milan-ASL/Milan-ASL%20V100R001C20SPC702/Ascend-cann-toolkit_8.0.0.alpha002_linux-"$(uname -i)".run
bash Ascend-cann-toolkit_8.0.0.alpha002_linux-"$(uname -i)".run --install

# install CANN Kernels
wget https://ascend-repo.obs.cn-east-2.myhuaweicloud.com/Milan-ASL/Milan-ASL%20V100R001C20SPC702/Ascend-cann-kernels-910b_8.0.0.alpha002_linux-"$(uname -i)".run
bash Ascend-cann-kernels-910b_8.0.0.alpha002_linux-"$(uname -i)".run --install

# set env variables
source /usr/local/Ascend/ascend-toolkit/set_env.sh
```  
| Requirement  | Minimum | Recommend      |
| ------------ | ------- | -------------- |
| CANN         | 8.0.RC1 | 8.0.0.alpha002 |
| torch        | 2.1.0   | 2.4.0          |
| torch-npu    | 2.1.0   | 2.4.0.post2    |
| deepspeed    | 0.13.2  | 0.13.2         |
| vllm-ascend  | -       | 0.7.3          |  
Remember to use `ASCEND_RT_VISIBLE_DEVICES` instead of `CUDA_VISIBLE_DEVICES` to specify the device to use.  
If you cannot infer model on NPU devices, try setting `do_sample: false` in the configurations.  
Download the pre-built Docker images: [32GB](http://mirrors.cn-central-221.ovaijisuan.com/detail/130.html) | [64GB](http://mirrors.cn-central-221.ovaijisuan.com/detail/131.html)