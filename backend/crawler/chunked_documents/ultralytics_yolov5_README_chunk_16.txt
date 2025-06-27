Repository: ultralytics/yolov5
Language: Python
Stars: 54285
Forks: 16994
-----
Use the pretrained YOLOv5s-cls.pt model to classify the image `bus.jpg`:  
```bash
# Run prediction
python classify/predict.py --weights yolov5s-cls.pt --source data/images/bus.jpg
```  
```python
# Load model from PyTorch Hub
model = torch.hub.load("ultralytics/yolov5", "custom", "yolov5s-cls.pt")
```