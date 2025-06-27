Repository: ultralytics/yolov5
Language: Python
Stars: 54285
Forks: 16994
-----
See the [YOLOv5 Docs](https://docs.ultralytics.com/yolov5/) for full documentation on training, testing, and deployment. See below for quickstart examples.  
<details open>
<summary>Install</summary>  
Clone the repository and install dependencies in a [**Python>=3.8.0**](https://www.python.org/) environment. Ensure you have [**PyTorch>=1.8**](https://pytorch.org/get-started/locally/) installed.  
```bash
# Clone the YOLOv5 repository
git clone https://github.com/ultralytics/yolov5

# Navigate to the cloned directory
cd yolov5

# Install required packages
pip install -r requirements.txt
```  
</details>  
<details open>
<summary>Inference with PyTorch Hub</summary>  
Use YOLOv5 via [PyTorch Hub](https://docs.ultralytics.com/yolov5/tutorials/pytorch_hub_model_loading/) for inference. [Models](https://github.com/ultralytics/yolov5/tree/master/models) are automatically downloaded from the latest YOLOv5 [release](https://github.com/ultralytics/yolov5/releases).  
```python
import torch

# Load a YOLOv5 model (options: yolov5n, yolov5s, yolov5m, yolov5l, yolov5x)
model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # Default: yolov5s

# Define the input image source (URL, local file, PIL image, OpenCV frame, numpy array, or list)
img = "https://ultralytics.com/images/zidane.jpg"  # Example image

# Perform inference (handles batching, resizing, normalization automatically)
results = model(img)

# Process the results (options: .print(), .show(), .save(), .crop(), .pandas())
results.print()  # Print results to console
results.show()  # Display results in a window
results.save()  # Save results to runs/detect/exp
```  
</details>  
<details>
<summary>Inference with detect.py</summary>  
The `detect.py` script runs inference on various sources. It automatically downloads [models](https://github.com/ultralytics/yolov5/tree/master/models) from the latest YOLOv5 [release](https://github.com/ultralytics/yolov5/releases) and saves the results to the `runs/detect` directory.  
```bash
# Run inference using a webcam
python detect.py --weights yolov5s.pt --source 0

# Run inference on a local image file
python detect.py --weights yolov5s.pt --source img.jpg

# Run inference on a local video file
python detect.py --weights yolov5s.pt --source vid.mp4

# Run inference on a screen capture
python detect.py --weights yolov5s.pt --source screen

# Run inference on a directory of images
python detect.py --weights yolov5s.pt --source path/to/images/

# Run inference on a text file listing image paths
python detect.py --weights yolov5s.pt --source list.txt

# Run inference on a text file listing stream URLs
python detect.py --weights yolov5s.pt --source list.streams

# Run inference using a glob pattern for images
python detect.py --weights yolov5s.pt --source 'path/to/*.jpg'

# Run inference on a YouTube video URL
python detect.py --weights yolov5s.pt --source 'https://youtu.be/LNwODJXcvt4'

# Run inference on an RTSP, RTMP, or HTTP stream
python detect.py --weights yolov5s.pt --source 'rtsp://example.com/media.mp4'
```  
</details>  
<details>
<summary>Training</summary>  
The commands below demonstrate how to reproduce YOLOv5 [COCO dataset](https://docs.ultralytics.com/datasets/detect/coco/) results. Both [models](https://github.com/ultralytics/yolov5/tree/master/models) and [datasets](https://github.com/ultralytics/yolov5/tree/master/data) are downloaded automatically from the latest YOLOv5 [release](https://github.com/ultralytics/yolov5/releases). Training times for YOLOv5n/s/m/l/x are approximately 1/2/4/6/8 days on a single [NVIDIA V100 GPU](https://www.nvidia.com/en-us/data-center/v100/). Using [Multi-GPU training](https://docs.ultralytics.com/yolov5/tutorials/multi_gpu_training/) can significantly reduce training time. Use the largest `--batch-size` your hardware allows, or use `--batch-size -1` for YOLOv5 [AutoBatch](https://github.com/ultralytics/yolov5/pull/5092). The batch sizes shown below are for V100-16GB GPUs.  
```bash
# Train YOLOv5n on COCO for 300 epochs
python train.py --data coco.yaml --epochs 300 --weights '' --cfg yolov5n.yaml --batch-size 128

# Train YOLOv5s on COCO for 300 epochs
python train.py --data coco.yaml --epochs 300 --weights '' --cfg yolov5s.yaml --batch-size 64

# Train YOLOv5m on COCO for 300 epochs
python train.py --data coco.yaml --epochs 300 --weights '' --cfg yolov5m.yaml --batch-size 40

# Train YOLOv5l on COCO for 300 epochs
python train.py --data coco.yaml --epochs 300 --weights '' --cfg yolov5l.yaml --batch-size 24

# Train YOLOv5x on COCO for 300 epochs
python train.py --data coco.yaml --epochs 300 --weights '' --cfg yolov5x.yaml --batch-size 16
```  
<img width="800" src="https://user-images.githubusercontent.com/26833433/90222759-949d8800-ddc1-11ea-9fa1-1c97eed2b963.png" alt="YOLOv5 Training Results">  
</details>  
<details open>
<summary>Tutorials</summary>  
- **[Train Custom Data](https://docs.ultralytics.com/yolov5/tutorials/train_custom_data/)** 🚀 **RECOMMENDED**: Learn how to train YOLOv5 on your own datasets.
- **[Tips for Best Training Results](https://docs.ultralytics.com/guides/model-training-tips/)** ☘️: Improve your model's performance with expert tips.
- **[Multi-GPU Training](https://docs.ultralytics.com/yolov5/tutorials/multi_gpu_training/)**: Speed up training using multiple GPUs.
- **[PyTorch Hub Integration](https://docs.ultralytics.com/yolov5/tutorials/pytorch_hub_model_loading/)** 🌟 **NEW**: Easily load models using PyTorch Hub.
- **[Model Export (TFLite, ONNX, CoreML, TensorRT)](https://docs.ultralytics.com/yolov5/tutorials/model_export/)** 🚀: Convert your models to various deployment formats like [ONNX](https://onnx.ai/) or [TensorRT](https://developer.nvidia.com/tensorrt).
- **[NVIDIA Jetson Deployment](https://docs.ultralytics.com/guides/nvidia-jetson/)** 🌟 **NEW**: Deploy YOLOv5 on [NVIDIA Jetson](https://developer.nvidia.com/embedded-computing) devices.
- **[Test-Time Augmentation (TTA)](https://docs.ultralytics.com/yolov5/tutorials/test_time_augmentation/)**: Enhance prediction accuracy with TTA.
- **[Model Ensembling](https://docs.ultralytics.com/yolov5/tutorials/model_ensembling/)**: Combine multiple models for better performance.
- **[Model Pruning/Sparsity](https://docs.ultralytics.com/yolov5/tutorials/model_pruning_and_sparsity/)**: Optimize models for size and speed.
- **[Hyperparameter Evolution](https://docs.ultralytics.com/yolov5/tutorials/hyperparameter_evolution/)**: Automatically find the best training hyperparameters.
- **[Transfer Learning with Frozen Layers](https://docs.ultralytics.com/yolov5/tutorials/transfer_learning_with_frozen_layers/)**: Adapt pretrained models to new tasks efficiently using [transfer learning](https://www.ultralytics.com/glossary/transfer-learning).
- **[Architecture Summary](https://docs.ultralytics.com/yolov5/tutorials/architecture_description/)** 🌟 **NEW**: Understand the YOLOv5 model architecture.
- **[Ultralytics HUB Training](https://www.ultralytics.com/hub)** 🚀 **RECOMMENDED**: Train and deploy YOLO models using Ultralytics HUB.
- **[ClearML Logging](https://docs.ultralytics.com/yolov5/tutorials/clearml_logging_integration/)**: Integrate with [ClearML](https://clear.ml/) for experiment tracking.
- **[Neural Magic DeepSparse Integration](https://docs.ultralytics.com/yolov5/tutorials/neural_magic_pruning_quantization/)**: Accelerate inference with DeepSparse.
- **[Comet Logging](https://docs.ultralytics.com/yolov5/tutorials/comet_logging_integration/)** 🌟 **NEW**: Log experiments using [Comet ML](https://www.comet.com/site/).  
</details>