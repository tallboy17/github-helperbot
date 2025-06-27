Repository: ultralytics/ultralytics
Language: Python
Stars: 42122
Forks: 8205
-----
You can use Ultralytics YOLO directly from the Command Line Interface (CLI) with the `yolo` command:  
```bash
# Predict using a pretrained YOLO model (e.g., YOLO11n) on an image
yolo predict model=yolo11n.pt source='https://ultralytics.com/images/bus.jpg'
```  
The `yolo` command supports various tasks and modes, accepting additional arguments like `imgsz=640`. Explore the YOLO [CLI Docs](https://docs.ultralytics.com/usage/cli/) for more examples.