Repository: ultralytics/yolov5
Language: Python
Stars: 54285
Forks: 16994
-----
Export trained YOLOv5s-cls, ResNet50, and EfficientNet_b0 models to ONNX and TensorRT formats:  
```bash
# Export models
python export.py --weights yolov5s-cls.pt resnet50.pt efficientnet_b0.pt --include onnx engine --img 224
```  
</details>