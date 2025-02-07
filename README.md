# YOLO11 Face Detection - Guia de Uso

Este repositório fornece scripts para treinamento e inferência de um modelo YOLO para detecção de rostos.

---

## Requisitos

Antes de iniciar, certifique-se de ter as seguintes versões instaladas:

### Python e Pip

- **Python**: 3.12.7
- **Pip**: 25.0

Comandos para verificação:

```sh
python --version
pip --version
```

### PyTorch e CUDA

- **PyTorch**: 2.5.1+cu121
- **CUDA**: 12.1
- **NVCC (CUDA Compiler)**: 12.1.66

Comandos para verificação:

```sh
python -c "import torch; print(torch.__version__); print(torch.version.cuda)"
nvcc --version
```

---

## Instalação do Ambiente

### 1. Instalação do Python e Pip

Baixe e instale o **Python 3.12.7** a partir do site oficial:

- [Download Python](https://www.python.org/downloads/release/python-3127/)

### 2. Instalação do CUDA e CuDNN

Baixe e instale as versões compatíveis do CUDA e CuDNN:

- **CUDA 12.1**: [Download CUDA](https://developer.nvidia.com/cuda-12-1-download-archive)
- **CuDNN para CUDA 12.1**: [Download CuDNN](https://developer.nvidia.com/cudnn)

### 3. Instalação do PyTorch

Instale a versão correta do PyTorch com suporte ao CUDA 12.1:

```sh
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### 4. Clonar o Repositório e Criar o Ambiente Virtual

```sh
git clone [https://github.com/seu-repositorio.git](https://github.com/pauloruszel/yolo11_face_detection.git)
cd yolo11_face_detection
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate  # Windows
```

---

## Execução dos Scripts

### 1. Converter as Labels para YOLO

Este script converte as anotações do dataset WIDER FACE para o formato do YOLO.

```sh
python scripts/convert_wider_to_yolo.py
```

### 2. Corrigir Labels Inconsistentes

Este script verifica e corrige labels que possuam coordenadas fora dos limites permitidos pelo YOLO.

```sh
python scripts/fix_labels.py
```

### 3. Treinar o Modelo

O batch size será ajustado automaticamente com base na memória disponível da GPU.

- `--img 640`: Define o tamanho da imagem utilizada no treinamento.
- `--batch 4`: Define o tamanho do batch (pode ser ajustado automaticamente).
- `--epochs 100`: Quantidade de épocas de treinamento.
- `--data dataset.yaml`: Caminho para o arquivo de configuração do dataset.
- `--weights yolo11n.pt`: Modelo pré-treinado utilizado como base.
- `--device 0`: Define a GPU a ser utilizada (0 para a primeira GPU).
- `--name face_detection`: Nome do experimento.
- `--half`: Usa precision FP16 para reduzir consumo de memória.
- `--cache=ram`: Carrega as imagens na RAM para acelerar o treinamento.

```sh
python scripts/train.py --img 640 --batch 4 --epochs 100 --data "C:/caminho/yolo11_face_detection/dataset.yaml" --weights "C:/caminho/yolo11_face_detection/models/yolo11n.pt" --device 0 --name face_detection --half --cache=ram
```

### 4. Executar Inferência com Webcam

Este script utiliza a webcam para realizar a detecção em tempo real.

```sh
python scripts/webcam_detect.py
```

### 5. Testar o Modelo em uma Imagem

Este script aplica a detecção em uma imagem específica.

```sh
python scripts/detection.py --image datasets/images/val/alguma_imagem.jpg
```

---

## Estrutura do Diretório

```
.
├── datasets/
│   ├── images/
│   │   ├── train/
│   │   ├── val/
│   ├── labels/
│       ├── train/
│       ├── val/
├── models/
├── scripts/
│   ├── train.py
│   ├── webcam_detect.py
│   ├── detection.py
│   ├── convert_wider_to_yolo.py
│   ├── fix_labels.py
├── yolo11n.pt
└── README.md
```

---

## Dicas de Otimização

- **Ajuste o Batch Size**: O batch size é ajustado automaticamente para evitar **out of memory (OOM)** na GPU.
- **Utilize `--cache=ram`**: Acelera o treinamento carregando as imagens na memória RAM.
- **Monitore a GPU**:
  ```sh
  nvidia-smi
  ```
- **Caso encontre erros de CUDA**, tente reiniciar a GPU com:
  ```sh
  nvidia-smi --gpu-reset
  ```

---

Caso encontre problemas, verifique se todas as versões dos pacotes estão compatíveis e atualizadas. Boa sorte no treinamento! 🚀
