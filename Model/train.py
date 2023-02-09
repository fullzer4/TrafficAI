import argparse
import torch
from ultralytics import YOLO
from roboflow import Roboflow
import subprocess
import os
from dotenv import load_dotenv

HOME = os.getcwd()

print(HOME)

load_dotenv()

apikey = os.getenv("api_key")

parser = argparse.ArgumentParser(description='Descrição')

parser.add_argument('-gpu', action='store_true', help='Run model in GPU')
parser.add_argument('-cpu', action='store_true', help='Run model in CPU')
parser.add_argument('-train', action='store_true', help='Run model train and import dataset')
parser.add_argument('-data', action='store_true', help='Run model train and import dataset')


args = parser.parse_args()

class Starter:
    def __init__(self):

        if args.gpu and args.cpu:
            print('Error: both -gpu and -cpu cannot be used together')
            exit(1)
        elif args.gpu:
            modeLine = ['yolo', 'checks']
            mode = subprocess.run(modeLine, capture_output=True, text=True)
            print(mode)
            if(torch.cuda.is_available()):
                print('Running GPU...')
        elif args.cpu:
            import os
            os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
        else:
            print('use -cpu or -gpu to run')
        
class data:
    def __init__(self):
        if args.data:
            
            modeLine = ['yolo', 'checks']
            mode = subprocess.run(modeLine, capture_output=True, text=True)
            print(mode)    
            
            rf = Roboflow(api_key=apikey)
            project = rf.workspace("gaurigodghase-gmail-com").project("vehicles-openimages-svzce")
            dataset = project.version(1).download("yolov8")
            
class train:
    def __init__(self):
        if args.train:
            torch.set_default_tensor_type('torch.FloatTensor')
            model = YOLO("yolov8s.pt")
            model.train(data="./vehicles-openimages-1/data.yaml", epochs=10)
            model.val()
            
            
if __name__ == '__main__':
    starter = Starter()
    data = data()
    train = train()