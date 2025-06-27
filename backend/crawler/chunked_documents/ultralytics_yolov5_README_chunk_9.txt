Repository: ultralytics/yolov5
Language: Python
Stars: 54285
Forks: 16994
-----
YOLOv5 segmentation training supports automatic download of the [COCO128-seg dataset](https://docs.ultralytics.com/datasets/segment/coco8-seg/) via the `--data coco128-seg.yaml` argument. For the full [COCO-segments dataset](https://docs.ultralytics.com/datasets/segment/coco/), download it manually using `bash data/scripts/get_coco.sh --train --val --segments` and then train with `python train.py --data coco.yaml`.  
```bash
# Train on a single GPU
python segment/train.py --data coco128-seg.yaml --weights yolov5s-seg.pt --img 640

# Train using Multi-GPU Distributed Data Parallel (DDP)
python -m torch.distributed.run --nproc_per_node 4 --master_port 1 segment/train.py --data coco128-seg.yaml --weights yolov5s-seg.pt --img 640 --device 0,1,2,3
```