import argparse
import torch
from ultralytics import YOLO
from IPython.display import Image
from IPython import display
from roboflow import Roboflow
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.getenv("api_key")

parser = argparse.ArgumentParser(description='Descrição')

parser.add_argument('-gpu', action='store_true', help='Run model in GPU')
parser.add_argument('-cpu', action='store_true', help='Run model in CPU')
parser.add_argument('-train', action='store_true', help='Run model train and import dataset')

args = parser.parse_args()

class Starter:
    def __init__(self):

        if args.gpu and args.cpu:
            print('Error: both -gpu and -cpu cannot be used together')
            exit(1)
        elif args.gpu:
            self.gpu_start()
        elif args.cpu:
            self.cpu_start()
        else:
            print('use -cpu or -gpu to run')

    def gpu_start(self):
        if(torch.cuda.is_available()):
            device = torch.device("cuda")
            print('Running GPU...')
        else:
            print('Running CPU because u dont have cuda install...')

    def cpu_start(self):
        device = torch.device("cpu")
        print('Running CPU...')
        
class train:
    def __init__(self):
        if args.train:
            
            display.clear_output()
            
            modeLine = ['yolo', 'checks']
            mode = subprocess.run(modeLine, capture_output=True, text=True)
            print(mode)    
            
            rf = Roboflow(api_key=apikey)
            project = rf.workspace("kgx-tgvum").project("traffic-flow-jgib7")
            self.dataset = project.version(2).download("yolov8")
            data_path = os.path.join(self.dataset.location, "data.yaml")
            trainLine = ['yolo', 'task=detect', 'mode=train', 'model=yolov8s.pt', f'data={data_path}', 'epochs=10', 'imgsz=256']
            train = subprocess.run(trainLine, capture_output=True, text=True)      
            print(train) 
        
if __name__ == '__main__':
    starter = Starter()
    train = train()