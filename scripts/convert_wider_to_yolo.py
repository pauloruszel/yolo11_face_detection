import os

# Definir os caminhos corretos
WIDER_FACE_LABELS_PATH = "C:/Users/rusze/Downloads/Estudo de IA/yolo11_face_detection/datasets/labels/wider_face_split"
YOLO_LABELS_TRAIN_PATH = "C:/Users/rusze/Downloads/Estudo de IA/yolo11_face_detection/datasets/labels/train"
YOLO_LABELS_VAL_PATH = "C:/Users/rusze/Downloads/Estudo de IA/yolo11_face_detection/datasets/labels/val"

# Criar as pastas de saída, se não existirem
os.makedirs(YOLO_LABELS_TRAIN_PATH, exist_ok=True)
os.makedirs(YOLO_LABELS_VAL_PATH, exist_ok=True)

def convert_wider_to_yolo(input_file, output_dir):
    if not os.path.exists(input_file):
        print(f"Erro: Arquivo {input_file} não encontrado!")
        return

    with open(input_file, "r") as f:
        lines = f.readlines()

    idx = 0
    while idx < len(lines):
        image_name = lines[idx].strip()

        # Verificar se a linha corresponde a um nome de imagem válido
        if not image_name.endswith(".jpg"):
            print(f"Aviso: Linha inesperada '{image_name}', pulando...")
            idx += 1
            continue
        
        idx += 1  # Próxima linha: número de faces

        if idx >= len(lines):
            print(f"Erro: Número de faces ausente para {image_name}")
            continue

        try:
            num_faces = int(lines[idx].strip())
            idx += 1
        except ValueError:
            print(f"Erro: Falha ao ler número de faces para {image_name}, pulando imagem...")
            continue

        yolo_labels = []
        for _ in range(num_faces):
            if idx >= len(lines):
                print(f"Erro: Faltam coordenadas para {image_name}")
                break

            parts = lines[idx].split()
            idx += 1

            if len(parts) < 4:
                print(f"Aviso: Linha inválida para bounding box em {image_name}, pulando...")
                continue

            x, y, w, h = map(int, parts[:4])

            # Converter para formato YOLO
            center_x = (x + w / 2) / 1024
            center_y = (y + h / 2) / 1024
            width = w / 1024
            height = h / 1024

            yolo_labels.append(f"0 {center_x} {center_y} {width} {height}")

        # 🔹 Criar diretório se não existir
        image_folder = os.path.dirname(image_name)
        output_folder = os.path.join(output_dir, image_folder)
        os.makedirs(output_folder, exist_ok=True)

        # 🔹 Criar arquivo YOLO no diretório correto
        output_file = os.path.join(output_folder, os.path.basename(image_name).replace(".jpg", ".txt"))

        with open(output_file, "w") as f:
            f.write("\n".join(yolo_labels))

# Processar arquivos de anotações
train_file = os.path.join(WIDER_FACE_LABELS_PATH, "wider_face_train_bbx_gt.txt")
val_file = os.path.join(WIDER_FACE_LABELS_PATH, "wider_face_val_bbx_gt.txt")

if os.path.exists(train_file):
    convert_wider_to_yolo(train_file, YOLO_LABELS_TRAIN_PATH)
else:
    print(f"Erro: {train_file} não encontrado!")

if os.path.exists(val_file):
    convert_wider_to_yolo(val_file, YOLO_LABELS_VAL_PATH)
else:
    print(f"Erro: {val_file} não encontrado!")

print("Conversão concluída! Labels salvas corretamente.")