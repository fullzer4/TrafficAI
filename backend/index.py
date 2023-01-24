from flask import Flask, jsonify, request
import torch
from Model.yolov5.models.yolo import DetectionModel
from Model.yolov5.utils.dataloaders import LoadImages
from Model.yolov5.utils.general import non_max_suppression
import numpy as np

app = Flask(__name__)

# Carregando os pesos pré-treinados
weights_path = "./Model/yolov5/runs/train/exp2/weights/best.pt"
model = DetectionModel()
model.load_state_dict(torch.load(weights_path))
model.to("cuda")
model.eval()

@app.route("/detect", methods=["POST"])
def detect():
    # Lendo a imagem enviada na requisição
    image = request.files["image"].read()
    
    # Convertendo a imagem para formato PyTorch
    img = torch.from_numpy(np.frombuffer(image, np.uint8))
    
    # Passando a imagem pela rede YOLOv5s
    img = img.to("cuda")
    predictions = model(img)
    
    # Fazendo non-maximum suppression para remover bounding boxes duplicadas
    boxes = non_max_suppression(predictions)
    
    # Extraindo as classes detectadas
    classes = [i.split(" ")[0] for i in boxes[1]]
    
    # Retornando as classes detectadas na imagem
    return jsonify({"classes": classes})

if __name__ == "__main__":
    app.run()