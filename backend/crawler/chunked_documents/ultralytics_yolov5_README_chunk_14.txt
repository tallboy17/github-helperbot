Repository: ultralytics/yolov5
Language: Python
Stars: 54285
Forks: 16994
-----
YOLOv5 classification training supports automatic download for datasets like [MNIST](https://docs.ultralytics.com/datasets/classify/mnist/), [Fashion-MNIST](https://docs.ultralytics.com/datasets/classify/fashion-mnist/), [CIFAR10](https://docs.ultralytics.com/datasets/classify/cifar10/), [CIFAR100](https://docs.ultralytics.com/datasets/classify/cifar100/), [Imagenette](https://docs.ultralytics.com/datasets/classify/imagenette/), [Imagewoof](https://docs.ultralytics.com/datasets/classify/imagewoof/), and [ImageNet](https://docs.ultralytics.com/datasets/classify/imagenet/) using the `--data` argument. For example, start training on MNIST with `--data mnist`.  
```bash
# Train on a single GPU using CIFAR-100 dataset
python classify/train.py --model yolov5s-cls.pt --data cifar100 --epochs 5 --img 224 --batch 128

# Train using Multi-GPU DDP on ImageNet dataset
python -m torch.distributed.run --nproc_per_node 4 --master_port 1 classify/train.py --model yolov5s-cls.pt --data imagenet --epochs 5 --img 224 --device 0,1,2,3
```