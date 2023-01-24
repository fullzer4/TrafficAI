import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
import os
import itertools

model = torch.hub.load('ultralytics/yolov5', 'custom', path='./yolov5/runs/train/exp2/weights/best.pt', force_reload=True)

fig, ax = plt.subplots(2,4, figsize=(20,10))
imgnames = os.listdir("./data/images")

for x in itertools.product(range(2), range(4)):
    imgname = np.random.choice(imgnames)
    img = cv2.imread(f'./data/images/{imgname}')
    result = model(img)
    ax[x[0],x[1]].imshow(cv2.cvtColor(np.squeeze(result.render()), cv2.COLOR_BGR2RGB))