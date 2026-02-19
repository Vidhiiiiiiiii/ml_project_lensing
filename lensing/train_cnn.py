import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers,models
import matplotlib.pyplot as plt

IMG_SIZE = 128
BATCH_SIZE = 16

TRAIN_DIR="lensing/data/train"
VAL_DIR="lensing/data/val"

train_datagen=ImageDataGenerator(
    rescale=1./255,
    rotation_range=360,
    zoom_range=0.2,
    horizontal_flip=True,
    vertical_flip=True
)
val_datagen=ImageDataGenerator(
    rescale=1./255
)

train_data=train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=(IMG_SIZE,IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="binary"
)

val_data=val_datagen.flow_from_directory(
    VAL_DIR,
    target_size=(IMG_SIZE,IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="binary"
)

model=models.Sequential([
    layers.Conv2D(16,(3,3),activation="relu",
                  input_shape=(IMG_SIZE,IMG_SIZE,3)),
    layers.MaxPooling2D((2,2)),

    layers.Conv2D(32,(3,3),activation="relu"),

    layers.MaxPooling2D((2,2)),

    layers.Conv2D(64,(3,3),activation="relu"),

    layers.MaxPooling2D((2,2)),

    layers.Flatten(),

    layers.Dense(64,activation="relu"),

    layers.Dense(1,activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

history=model.fit(
    train_data,
    validation_data=val_data,
    epochs=20
)

model.save("lensing/lens_classifier.keras")

print("Model trained and saved successfully 🚀")

plt.plot(history.history["accuracy"],label="train accuracy")
plt.plot(history.history["val_accuracy"],label="val_accuracy")

plt.legend()
plt.title("Accuracy vs Epochs")
plt.show()

plt.plot(history.history["loss"],label="train loss")
plt.plot(history.history["val_loss"],label="val loss")

plt.legend()
plt.title("Loss vc Epochs")
plt.show()