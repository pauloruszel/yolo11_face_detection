import cv2
from ultralytics import YOLO

# ✅ Certifique-se de que o caminho do modelo está correto
model_path = "C:/Users/rusze/Downloads/Estudo de IA/yolo11_face_detection/runs/detect/train/weights/best.pt"

# ✅ Carregar o modelo treinado
model = YOLO(model_path)

# ✅ Iniciar a webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # ✅ Realizar a detecção
    results = model(frame)

    # ✅ Obter a imagem com as detecções desenhadas
    annotated_frame = results[0].plot()

    # ✅ Exibir o frame com as detecções
    cv2.imshow("Detecção de Faces - YOLO", annotated_frame)

    # ✅ Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ✅ Liberar recursos
cap.release()
cv2.destroyAllWindows()