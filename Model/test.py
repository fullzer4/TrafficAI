from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor

model = YOLO("runs/detect/train7/weights/best.pt")
model.predict(source="MVI_2378.MOV", show=True, conf=0.3)