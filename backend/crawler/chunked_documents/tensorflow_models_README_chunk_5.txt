Repository: tensorflow/models
Language: Python
Stars: 77575
Forks: 45570
-----
<details>  
1. Clone the GitHub repository:  
```shell
git clone https://github.com/tensorflow/models.git
```  
2. Add the top-level ***/models*** folder to the Python path.  
```shell
export PYTHONPATH=$PYTHONPATH:/path/to/models
```  
If you are using in a Windows environment, you may need to use the following command with PowerShell:
```shell
$env:PYTHONPATH += ":\path\to\models"
```  
If you are using a Colab notebook, please set the Python path with os.environ.  
```python
import os
os.environ['PYTHONPATH'] += ":/path/to/models"
```  
3. Install other dependencies  
```shell
pip3 install --user -r models/official/requirements.txt
```  
Finally, if you are using nlp packages, please also install
**tensorflow-text-nightly**:  
```shell
pip3 install tensorflow-text-nightly
```  
</details>