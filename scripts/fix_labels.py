import os

def fix_label_file(label_path):
    fixed_lines = []
    with open(label_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split()
            if len(parts) < 5:
                continue  # Ignorar linhas inválidas
            cls, x, y, w, h = map(float, parts)
            if x > 1 or y > 1 or w > 1 or h > 1:
                print(f"Corrigindo bounding box em {label_path}")
                x = min(x, 1.0)
                y = min(y, 1.0)
                w = min(w, 1.0)
                h = min(h, 1.0)
            fixed_lines.append(f"{cls} {x} {y} {w} {h}\n")

    with open(label_path, "w") as f:
        f.writelines(fixed_lines)

def fix_labels_in_folder(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt"):
                fix_label_file(os.path.join(root, file))

labels_train_path = "C:/Users/rusze/Downloads/Estudo de IA/yolo11_face_detection/datasets/labels/train"
labels_val_path = "C:/Users/rusze/Downloads/Estudo de IA/yolo11_face_detection/datasets/labels/val"

fix_labels_in_folder(labels_train_path)
fix_labels_in_folder(labels_val_path)

print("Correção das labels concluída!")