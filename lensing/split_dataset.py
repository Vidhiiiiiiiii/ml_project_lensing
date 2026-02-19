import os
import random
import shutil

BASE_DIR="lensing/data"
CLASSES=["lensed","unlensed"]
SPLIT_RATIO=0.8

for cls in CLASSES:
    source_folder=os.path.join(BASE_DIR,cls)

    train_folder=os.path.join(BASE_DIR,"train",cls)
    val_folder=os.path.join(BASE_DIR,"val",cls)

    os.makedirs(train_folder,exist_ok=True)
    os.makedirs(val_folder,exist_ok=True)

    images=os.listdir(source_folder)

    random.shuffle(images)

    split_index=int(len(images)*SPLIT_RATIO)

    train_images=images[:split_index]
    val_images=images[split_index:]

    for img in train_images:
        shutil.move(
            os.path.join(source_folder,img),
            os.path.join(train_folder,img)
        )
    for img in val_images:
        shutil.move(
            os.path.join(source_folder,img),
            os.path.join(val_folder,img)
        )
    print(f"{cls}: {len(train_images)} train, {len(val_images)} val")
