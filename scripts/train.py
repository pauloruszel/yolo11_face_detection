import torch
from ultralytics import YOLO

def train_yolo():
    model = YOLO("C:/Users/rusze/Downloads/Estudo de IA/yolo11_face_detection/models/yolo11n.pt")
    model.train(
        data="C:/Users/rusze/Downloads/Estudo de IA/yolo11_face_detection/dataset.yaml",
        epochs=200,
        batch=6,
        imgsz=640,
        device=torch.device("cuda:0")
    )

if __name__ == "__main__":
    train_yolo()