Repository: ultralytics/yolov5
Language: Python
Stars: 54285
Forks: 16994
-----
Validate the mask [mean Average Precision (mAP)](https://www.ultralytics.com/glossary/mean-average-precision-map) of YOLOv5s-seg on the COCO dataset:  
```bash
# Download COCO validation segments split (780MB, 5000 images)
bash data/scripts/get_coco.sh --val --segments

# Validate the model
python segment/val.py --weights yolov5s-seg.pt --data coco.yaml --img 640
```