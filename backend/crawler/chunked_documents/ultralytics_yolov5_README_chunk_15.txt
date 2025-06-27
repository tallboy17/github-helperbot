Repository: ultralytics/yolov5
Language: Python
Stars: 54285
Forks: 16994
-----
Validate the accuracy of the YOLOv5m-cls model on the ImageNet-1k validation dataset:  
```bash
# Download ImageNet validation split (6.3GB, 50,000 images)
bash data/scripts/get_imagenet.sh --val

# Validate the model
python classify/val.py --weights yolov5m-cls.pt --data ../datasets/imagenet --img 224
```