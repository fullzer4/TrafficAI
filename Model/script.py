from roboflow import Roboflow
import ultralytics
import yolox

rf = Roboflow(api_key="YG32Zd9Kcmc9muEmR5G4")
project = rf.workspace("roboflow-100").project("vehicles-q0x2v")
dataset = project.version(2).download("yolov8")