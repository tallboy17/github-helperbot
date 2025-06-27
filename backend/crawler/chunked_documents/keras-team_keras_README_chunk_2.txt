Repository: keras-team/keras
Language: Python
Stars: 63136
Forks: 19580
-----
Keras 3 is available on PyPI as `keras`. Note that Keras 2 remains available as the `tf-keras` package.  
1. Install `keras`:  
```
pip install keras --upgrade
```  
2. Install backend package(s).  
To use `keras`, you should also install the backend of choice: `tensorflow`, `jax`, or `torch`.
Note that `tensorflow` is required for using certain Keras 3 features: certain preprocessing layers
as well as `tf.data` pipelines.