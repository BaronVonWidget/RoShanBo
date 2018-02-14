from PIL import Image
import numpy as np
import os

p = os.listdir(".\Hands\Train\Paper")
r = os.listdir(".\Hands\Train\Rock")
s = os.listdir(".\Hands\Train\Scissors")
pT = os.listdir(".\Hands\Test\Paper")
rT = os.listdir(".\Hands\Test\Rock")
sT = os.listdir(".\Hands\Test\Scissors")
labels = []
features = []  # TODO Add new images for better learning


def append(a, b, c):
    for files in a:
        f = b + "\\" + files
        i = Image.open(f).convert('L').resize([60, 60])
        t = np.asarray(i).flatten().tolist()
        features.append(t)
        labels.append(c)


def pipetrain():
    append(r, ".\Hands\Train\Rock", 0)
    append(p, ".\Hands\Train\Paper", 1)
    append(s, ".\Hands\Train\Scissors", 2)
    feat_np = np.matrix(features).astype(np.float32)
    lab_np = np.array(labels).astype(dtype=np.uint8)
    lab_onehot = (np.arange(3) == lab_np[:, None]).astype(np.float32)
    return lab_onehot, feat_np


def pipetest():
    append(rT, ".\Hands\Test\Rock", 0)
    append(pT, ".\Hands\Test\Paper", 1)
    append(sT, ".\Hands\Test\Scissors", 2)
    feat_np = np.matrix(features).astype(np.float32)
    lab_np = np.array(labels).astype(dtype=np.uint8)
    lab_onehot = (np.arange(3) == lab_np[:, None]).astype(np.float32)
    return lab_onehot, feat_np
