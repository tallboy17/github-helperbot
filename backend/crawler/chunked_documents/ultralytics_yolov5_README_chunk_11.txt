Repository: ultralytics/yolov5
Language: Python
Stars: 54285
Forks: 16994
-----
Use the pretrained YOLOv5m-seg.pt model to perform segmentation on `bus.jpg`:  
```bash
# Run prediction
python segment/predict.py --weights yolov5m-seg.pt --source data/images/bus.jpg
```  
```python
# Load model from PyTorch Hub (Note: Inference support might vary)
model = torch.hub.load("ultralytics/yolov5", "custom", "yolov5m-seg.pt")
```  
| ![Zidane Segmentation Example](https://user-images.githubusercontent.com/26833433/203113421-decef4c4-183d-4a0a-a6c2-6435b33bc5d3.jpg) | ![Bus Segmentation Example](https://user-images.githubusercontent.com/26833433/203113416-11fe0025-69f7-4874-a0a6-65d0bfe2999a.jpg) |
| :-----------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------: |