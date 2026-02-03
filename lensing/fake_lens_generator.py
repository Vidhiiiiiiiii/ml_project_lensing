import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("lensing/data/lensed",exist_ok=True)
os.makedirs("lensing/data/unlensed",exist_ok=True)

def generate_lensed(size=128):
    img=np.zeros((size,size))

    cx,cy=np.random.randint(40,88,size=2)

    for i in range(size):
        for j in range(size):
            dist=np.sqrt((i-cx)**2 + (j-cy)**2)
            if 18<dist<23:
                img[i,j]=1

    img+=np.random.normal(0,0.05,img.shape)

    return img

def generate_unlensed(size=128):
    img=np.zeros((size,size))
     
    cx,cy=size//2,size//2

    for i in range(size):
        for j in range(size):
            dist=np.sqrt((i-cx)**2 + (j-cy)**2)

            if dist<15:
                img[i,j]=1
# stronger random noise
    img +=np.random.normal(0,0.15,img.shape)
    # random brightness change
    img=img*np.random.uniform(0.7,1.3)
    # clip values (keep btw 0nd1)
    img=np.clip(img,0,1)
    return img
NUM_IMAGES = 50

for i in range(NUM_IMAGES):
    lens=generate_lensed()
    normal=generate_unlensed()

    plt.imsave(f"lensing/data/lensed/lens_{i}.png",lens,cmap="inferno")
    plt.imsave(f"lensing/data/unlensed/normal_{i}.png",normal,cmap="inferno")

print("Fake lensing dataset created 🚀")

