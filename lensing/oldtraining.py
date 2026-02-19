import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout,BatchNormalization
import os

DATA_DIR="lensing/data"
IMG_SIZE=128
BATCH_SIZE=8

datagen=ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,

    rotation_range=30,
    zoom_range=0.3,
    shear_range=0.2,
    width_shift_range=0.1,
    height_shift_range=0.1,

    horizontal_flip=True,
    brightness_range=[0.7,1.3]
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
    Conv2D(32,(3,3), activation="relu", input_shape=(IMG_SIZE,IMG_SIZE,3)),
    BatchNormalization(),
    MaxPooling2D(2,2),

    Conv2D(64,(3,3), activation="relu"),
    BatchNormalization(),
    MaxPooling2D(2,2),

    # Conv2D(128,(3,3), activation="relu"),
    # BatchNormalization(),
    # MaxPooling2D(2,2),

    Flatten(),

    # Dense(128, activation="relu"),
    # Dropout(0.5),
    Dense(64, activation="relu"),
    Dropout(0.4),

    Dense(1, activation="sigmoid")
])


model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.summary()

early_stop=EarlyStopping(
    monitor="val_loss",
    patience=3,
    restore_best_weights=True
)

history=model.fit(
    train_data,
    validation_data=val_data,
    epochs=20,
    callbacks=[early_stop]
)

model.save("lensing/lens_classifier.keras")
print(train_data.class_indices)

print("Model trained & saved 🚀")