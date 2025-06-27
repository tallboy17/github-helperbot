Repository: tensorflow/models
Language: Python
Stars: 77575
Forks: 45570
-----
The TensorFlow Model Garden is a repository with a number of different
implementations of state-of-the-art (SOTA) models and modeling solutions for
TensorFlow users. We aim to demonstrate the best practices for modeling so that
TensorFlow users can take full advantage of TensorFlow for their research and
product development.  
To improve the transparency and reproducibility of our models, training logs on
[TensorBoard.dev](https://tensorboard.dev) are also provided for models to the
extent possible though not all models are suitable.  
| Directory | Description |
|-----------|-------------|
| [official](official) | • A collection of example implementations for SOTA models using the latest TensorFlow 2's high-level APIs<br />• Officially maintained, supported, and kept up to date with the latest TensorFlow 2 APIs by TensorFlow<br />• Reasonably optimized for fast performance while still being easy to read<br /> For more details on the capabilities, check the guide on the [Model-garden](https://www.tensorflow.org/tfmodels)|
| [research](research) | • A collection of research model implementations in TensorFlow 1 or 2 by researchers<br />• Maintained and supported by researchers |
| [community](community) | • A curated list of the GitHub repositories with machine learning models and implementations powered by TensorFlow 2 |
| [orbit](orbit) | • A flexible and lightweight library that users can easily use or fork when writing customized training loop code in TensorFlow 2.x. It seamlessly integrates with `tf.distribute` and supports running on different device types (CPU, GPU, and TPU). |