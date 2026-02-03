import tensorflow as tf
import numpy as np
import cv2
import os
from tensorflow.keras.preprocessing import image

MODEL_PATH="lensing/lens_classifier.keras"
IMG_SIZE=128

model=tf.keras.models.load_model(MODEL_PATH)

print("Model loaded ✅")

def predict_image(img_path):
    img=image.load_img(img_path,target_size=(IMG_SIZE,IMG_SIZE))
    img=image.img_to_array(img)
    # img=cv2.imread(img_path)

    # img=cv2.resize(img,(IMG_SIZE,IMG_SIZE))
    
    img=img/255.0

    img = np.expand_dims(img,axis=0)

    pred = model.predict(img)[0][0]

    if pred>0.5:
        print(img_path,"→ ✨ NORMAL (", round(pred,2), ")")
    else:
        print(img_path,"→ 🌌 LENSED (", round(pred,2), ")")

LENSED_DIR="lensing/data/lensed"
NORMAL_DIR="lensing/data/unlensed"

print("\nTesting Lensed Images:")

for f in os.listdir(LENSED_DIR)[:5]:
    predict_image(os.path.join(LENSED_DIR,f))


print("\nTesting Normal Images:")

for f in os.listdir(NORMAL_DIR)[:5]:
    predict_image(os.path.join(NORMAL_DIR,f))
