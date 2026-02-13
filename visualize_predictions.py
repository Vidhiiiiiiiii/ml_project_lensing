import tensorflow as tf
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

MODEL_PATH="lensing/lens_classifier.keras"
IMG_SIZE=128

model=tf.keras.models.load_model(MODEL_PATH)

def load_image(path):
    img=cv2.imread(path)
    img=cv2.resize(img,(IMG_SIZE,IMG_SIZE))
    img=img/255.0
    img=np.expand_dims(img,axis=0)
    return img
def show_predictions(folder,label_name):
    files=os.listdir(folder)[:6]

    plt.figure(figsize=(10,6))

    for i,f in enumerate(files):
        path=os.path.join(folder,f)

        img=load_image(path)

        pred=model.predict(img)[0][0]

        plt.subplot(2,3,i+1)

        raw=cv2.imread(path)

        plt.imshow(raw,cmap="inferno")

        if pred>0.5:
            text=f"LENSED ({pred:.2f})"
        else:
            text=f"NORMAL ({pred:.2f})"
        
        plt.title(text)

    plt.suptitle(label_name)

    plt.show()
    
show_predictions("lensing/data/lensed","Lensed Images")
show_predictions("lensing/data/unlensed","Unlensed Images")
