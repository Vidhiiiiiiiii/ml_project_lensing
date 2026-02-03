import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
import os

DATA_DIR="lensing/data"
IMG_SIZE=128
BATCH_SIZE=8

datagen=ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

train_data=datagen.flow_from_directory(
    DATA_DIR,
    target_size=(IMG_SIZE,IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="binary",
    subset="training"
)

val_data=datagen.flow_from_directory(
    DATA_DIR,
    target_size=(IMG_SIZE,IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="binary",
    subset="validation"
)

model=Sequential([
    Conv2D(16,(3,3), activation="relu", input_shape=(IMG_SIZE,IMG_SIZE,3)),
    MaxPooling2D(2,2),

    Conv2D(32,(3,3), activation="relu"),
    MaxPooling2D(2,2),

    Flatten(),

    Dense(64, activation="relu"),
    Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.summary()

history=model.fit(
    train_data,
    validation_data=val_data,
    epochs=10
)

model.save("lensing/lens_classifier.keras")
print(train_data.class_indices)

print("Model trained & saved 🚀")