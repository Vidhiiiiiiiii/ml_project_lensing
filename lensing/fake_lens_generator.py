import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

os.makedirs("lensing/data/lensed",exist_ok=True)
os.makedirs("lensing/data/unlensed",exist_ok=True)

SIZE=128

def random_galexy_bg(size):

    bg=np.random.normal(0.1,0.05,(size,size))

    for _ in range(np.random.randint(3,8)):
        x=np.random.randint(0,size)
        y=np.random.randint(0,size)

        cv2.circle(bg,(x,y),np.random.randint(1,3),0.8,-1)
    return bg

def generate_lensed():
    
    img=random_galexy_bg(SIZE)

    cx=np.random.randint(40,88)
    cy=np.random.randint(40,88)

    radius=np.random.randint(18,25)
    thickness=np.random.randint(3,7)

    for i in range(SIZE):
        for j in range(SIZE):
            dist=np.sqrt((i-cx)**2+(j-cy)**2)

            if radius<dist<radius+thickness:
                brightness=np.random.uniform(0.7,1.2)
                img[i,j]+=brightness
    img=cv2.GaussianBlur(img,(5,5),0)

    img+=np.random.normal(0,0.05,img.shape)

    img=np.clip(img,0,1)

    return img

def generate_unlensed():

    img=random_galexy_bg(SIZE)

    cx=SIZE//2
    cy=SIZE//2

    r=np.random.randint(10,18)

    cv2.circle(img,(cx,cy),r,0.6,-1)

    img=cv2.GaussianBlur(img,(5,5),0)

    img+=np.random.normal(0,0.05,img.shape)

    img=np.clip(img,0,1)

    return img

NUM=100

for i in range(NUM):

    lens=generate_lensed()
    normal=generate_unlensed()

    plt.imsave(f"lensing/data/lensed/lens_{i}.png",lens,cmap="inferno")
    plt.imsave(f"lensing/data/unlensed/normal_{i}.png",normal,cmap="inferno")


print("Advanced fake lens dataset created 🚀")
