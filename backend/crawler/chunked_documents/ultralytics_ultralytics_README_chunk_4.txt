Repository: ultralytics/ultralytics
Language: Python
Stars: 42122
Forks: 8205
-----
Ultralytics YOLO can also be integrated directly into your Python projects. It accepts the same [configuration arguments](https://docs.ultralytics.com/usage/cfg/) as the CLI:  
```python
from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Train the model on the COCO8 dataset for 100 epochs
train_results = model.train(
data="coco8.yaml",  # Path to dataset configuration file
epochs=100,  # Number of training epochs
imgsz=640,  # Image size for training
device="cpu",  # Device to run on (e.g., 'cpu', 0, [0,1,2,3])
)

# Evaluate the model's performance on the validation set
metrics = model.val()

# Perform object detection on an image
results = model("path/to/image.jpg")  # Predict on an image
results[0].show()  # Display results

# Export the model to ONNX format for deployment
path = model.export(format="onnx")  # Returns the path to the exported model
```  
Discover more examples in the YOLO [Python Docs](https://docs.ultralytics.com/usage/python/).  
</details>