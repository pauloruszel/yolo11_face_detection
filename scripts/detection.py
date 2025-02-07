from ultralytics import YOLO
import cv2

# Carregar o modelo treinado
model = YOLO("models/yolo_face_detection/weights/best.pt")

# Testar em uma imagem específica
image_path = "datasets/images/val/images/alguma_imagem.jpg"  # Escolha uma imagem do dataset
results = model(image_path)

# Exibir a imagem com as detecções
results[0].show()