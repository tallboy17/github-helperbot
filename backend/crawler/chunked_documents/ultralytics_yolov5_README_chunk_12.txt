Repository: ultralytics/yolov5
Language: Python
Stars: 54285
Forks: 16994
-----
Export the YOLOv5s-seg model to ONNX and TensorRT formats:  
```bash
# Export model
python export.py --weights yolov5s-seg.pt --include onnx engine --img 640 --device 0
```  
</details>