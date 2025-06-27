Repository: deepspeedai/DeepSpeed
Language: Python
Stars: 39026
Forks: 4426
-----
We regularly push releases to [PyPI](https://pypi.org/project/deepspeed/) and encourage users to install from there in most cases.  
```bash
pip install deepspeed
```  
After installation, you can validate your install and see which extensions/ops
your machine is compatible with via the DeepSpeed environment report.  
```bash
ds_report
```  
If you would like to pre-install any of the DeepSpeed extensions/ops (instead
of JIT compiling) or install pre-compiled ops via PyPI please see our [advanced
installation instructions](https://www.deepspeed.ai/tutorials/advanced-install/).