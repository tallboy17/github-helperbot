Repository: pandas-dev/pandas
Language: Python
Stars: 45747
Forks: 18598
-----
To install pandas from source you need [Cython](https://cython.org/) in addition to the normal
dependencies above. Cython can be installed from PyPI:  
```sh
pip install cython
```  
In the `pandas` directory (same one where you found this file after
cloning the git repo), execute:  
```sh
pip install .
```  
or for installing in [development mode](https://pip.pypa.io/en/latest/cli/pip_install/#install-editable):  
```sh
python -m pip install -ve . --no-build-isolation -Ceditable-verbose=true
```  
See the full instructions for [installing from source](https://pandas.pydata.org/docs/dev/development/contributing_environment.html).