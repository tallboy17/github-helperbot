Repository: keras-team/keras
Language: Python
Stars: 63136
Forks: 19580
-----
You can export the environment variable `KERAS_BACKEND` or you can edit your local config file at `~/.keras/keras.json`
to configure your backend. Available backend options are: `"tensorflow"`, `"jax"`, `"torch"`, `"openvino"`. Example:  
```
export KERAS_BACKEND="jax"
```  
In Colab, you can do:  
```python
import os
os.environ["KERAS_BACKEND"] = "jax"

import keras
```  
**Note:** The backend must be configured before importing `keras`, and the backend cannot be changed after
the package has been imported.  
**Note:** The OpenVINO backend is an inference-only backend, meaning it is designed only for running model
predictions using `model.predict()` method.