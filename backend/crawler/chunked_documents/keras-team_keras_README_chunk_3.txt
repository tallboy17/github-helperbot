Repository: keras-team/keras
Language: Python
Stars: 63136
Forks: 19580
-----
Keras 3 is compatible with Linux and MacOS systems. For Windows users, we recommend using WSL2 to run Keras.
To install a local development version:  
1. Install dependencies:  
```
pip install -r requirements.txt
```  
2. Run installation command from the root directory.  
```
python pip_build.py --install
```  
3. Run API generation script when creating PRs that update `keras_export` public APIs:  
```
./shell/api_gen.sh
```