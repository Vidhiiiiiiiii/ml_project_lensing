import os
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

INPUT = "all_fits"
OUTPUT = "all_png"

os.makedirs(OUTPUT, exist_ok=True)

count = 0


for file in os.listdir(INPUT):

    if not file.lower().endswith(".fits"):
        continue

    path = os.path.join(INPUT, file)

    try:
        hdul = fits.open(path)
        data = hdul[0].data
        hdul.close()

        if data is None:
            continue

        # Normalize brightness
        data = data - np.min(data)
        data = data / np.max(data)

        out_name = file.replace(".fits", ".png")
        out_path = os.path.join(OUTPUT, out_name)

        plt.imsave(out_path, data, cmap="gray")

        count += 1

    except Exception as e:
        print("Error:", file, e)


print("Converted", count, "images to PNG ✅")

