Repository: hiyouga/LLaMA-Factory
Language: Python
Stars: 52604
Forks: 6439
-----
To use [SwanLab](https://github.com/SwanHubX/SwanLab) for logging experimental results, you need to add the following arguments to yaml files.  
```yaml
use_swanlab: true
swanlab_run_name: test_run # optional
```  
When launching training tasks, you can log in to SwanLab in three ways:  
1. Add `swanlab_api_key=<your_api_key>` to the yaml file, and set it to your [API key](https://swanlab.cn/settings).
2. Set the environment variable `SWANLAB_API_KEY` to your [API key](https://swanlab.cn/settings).
3. Use the `swanlab login` command to complete the login.