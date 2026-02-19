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

def generate_lensed(size=128):
    
    img=random_galexy_bg(size)

    cx=np.random.randint(30,size-30)
    cy=np.random.randint(30,size-30)

    rx=np.random.randint(18,25)
    ry=np.random.randint(12,22)

    start_angle=np.random.uniform(0,2*np.pi)
    arc_length=np.random.uniform(np.pi/6,np.pi/2)
    end_angle=start_angle+arc_length

    thickness=np.random.randint(2,5)

    for angle in np.linspace(start_angle,end_angle,200):

        for t in range(thickness):

            x=int(cx+(rx+t)*np.cos(angle))
            y=int(cy+(ry+t)*np.sin(angle))

            if 0<=x<size and 0<=y<size:

                brightness=np.random.uniform(0.6,1.0)
                img[y,x]+=brightness

    if np.random.rand()>0.5:

        shift=np.random.randint(5,15)

        for angle in np.linspace(start_angle,end_angle,150):
            
            x=int(cx+(rx+shift)*np.cos(angle))
            y=int(cy+(ry+shift)*np.sin(angle))

            if 0<=x<size and 0<=y<size:

                img[y,x]+=np.random.uniform(0.4,0.8)

    img=cv2.GaussianBlur(img,(5,5),0)

    img+=np.random.normal(0,0.05, img.shape)

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
