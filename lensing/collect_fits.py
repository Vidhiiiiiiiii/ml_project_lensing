import os
import shutil

SOURCE = "Castles"      # Your main folder
DEST = "all_fits"       # New folder

os.makedirs(DEST, exist_ok=True)

count = 0

for root, dirs, files in os.walk(SOURCE):

    for file in files:

        if file.lower().endswith(".fits"):

            src = os.path.join(root, file)

            # Rename to avoid duplicates
            new_name = root.replace("\\", "_").replace("/", "_") + "_" + file
            dst = os.path.join(DEST, new_name)

            shutil.copy(src, dst)

            count += 1


print("Collected", count, "FITS files ✅")
