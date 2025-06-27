Repository: ultralytics/yolov5
Language: Python
Stars: 54285
Forks: 16994
-----
The YOLOv5 [release v7.0](https://github.com/ultralytics/yolov5/releases/v7.0) introduced [instance segmentation](https://docs.ultralytics.com/tasks/segment/) models that achieve state-of-the-art performance. These models are designed for easy training, validation, and deployment. For full details, see the [Release Notes](https://github.com/ultralytics/yolov5/releases/v7.0) and explore the [YOLOv5 Segmentation Colab Notebook](https://github.com/ultralytics/yolov5/blob/master/segment/tutorial.ipynb) for quickstart examples.  
<details>
<summary>Segmentation Checkpoints</summary>  
<div align="center">
<a align="center" href="https://www.ultralytics.com/yolo" target="_blank">
<img width="800" src="https://user-images.githubusercontent.com/61612323/204180385-84f3aca9-a5e9-43d8-a617-dda7ca12e54a.png" alt="YOLOv5 Segmentation Performance Chart"></a>
</div>  
YOLOv5 segmentation models were trained on the [COCO dataset](https://docs.ultralytics.com/datasets/segment/coco/) for 300 epochs at an image size of 640 pixels using A100 GPUs. Models were exported to [ONNX](https://onnx.ai/) FP32 for CPU speed tests and [TensorRT](https://developer.nvidia.com/tensorrt) FP16 for GPU speed tests. All speed tests were conducted on Google [Colab Pro](https://colab.research.google.com/signup) notebooks for reproducibility.  
| Model                                                                                      | Size<br><sup>(pixels) | mAP<sup>box<br>50-95 | mAP<sup>mask<br>50-95 | Train Time<br><sup>300 epochs<br>A100 (hours) | Speed<br><sup>ONNX CPU<br>(ms) | Speed<br><sup>TRT A100<br>(ms) | Params<br><sup>(M) | FLOPs<br><sup>@640 (B) |
| ------------------------------------------------------------------------------------------ | --------------------- | -------------------- | --------------------- | --------------------------------------------- | ------------------------------ | ------------------------------ | ------------------ | ---------------------- |
| [YOLOv5n-seg](https://github.com/ultralytics/yolov5/releases/download/v7.0/yolov5n-seg.pt) | 640                   | 27.6                 | 23.4                  | 80:17                                         | **62.7**                       | **1.2**                        | **2.0**            | **7.1**                |
| [YOLOv5s-seg](https://github.com/ultralytics/yolov5/releases/download/v7.0/yolov5s-seg.pt) | 640                   | 37.6                 | 31.7                  | 88:16                                         | 173.3                          | 1.4                            | 7.6                | 26.4                   |
| [YOLOv5m-seg](https://github.com/ultralytics/yolov5/releases/download/v7.0/yolov5m-seg.pt) | 640                   | 45.0                 | 37.1                  | 108:36                                        | 427.0                          | 2.2                            | 22.0               | 70.8                   |
| [YOLOv5l-seg](https://github.com/ultralytics/yolov5/releases/download/v7.0/yolov5l-seg.pt) | 640                   | 49.0                 | 39.9                  | 66:43 (2x)                                    | 857.4                          | 2.9                            | 47.9               | 147.7                  |
| [YOLOv5x-seg](https://github.com/ultralytics/yolov5/releases/download/v7.0/yolov5x-seg.pt) | 640                   | **50.7**             | **41.4**              | 62:56 (3x)                                    | 1579.2                         | 4.5                            | 88.8               | 265.7                  |  
- All checkpoints were trained for 300 epochs using the SGD optimizer with `lr0=0.01` and `weight_decay=5e-5` at an image size of 640 pixels, using default settings.<br>Training runs are logged at [https://wandb.ai/glenn-jocher/YOLOv5_v70_official](https://wandb.ai/glenn-jocher/YOLOv5_v70_official).
- **Accuracy** values represent single-model, single-scale performance on the COCO dataset.<br>Reproduce using: `python segment/val.py --data coco.yaml --weights yolov5s-seg.pt`
- **Speed** metrics are averaged over 100 inference images using a [Colab Pro A100 High-RAM instance](https://colab.research.google.com/signup). Values indicate inference speed only (NMS adds approximately 1ms per image).<br>Reproduce using: `python segment/val.py --data coco.yaml --weights yolov5s-seg.pt --batch 1`
- **Export** to ONNX (FP32) and TensorRT (FP16) was performed using `export.py`.<br>Reproduce using: `python export.py --weights yolov5s-seg.pt --include engine --device 0 --half`  
</details>  
<details>
<summary>Segmentation Usage Examples &nbsp;<a href="https://colab.research.google.com/github/ultralytics/yolov5/blob/master/segment/tutorial.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a></summary>