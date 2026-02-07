import requests
import os

# Example Hubble/NASA image URLs (you can extend later)
URLS = [
    "https://images-assets.nasa.gov/image/PIA12110/PIA12110~orig.jpg",
    "https://images-assets.nasa.gov/image/GSFC_20171208_Archive_e000394/GSFC_20171208_Archive_e000394~orig.jpg",
    "https://images-assets.nasa.gov/image/GSFC_20171208_Archive_e001651/GSFC_20171208_Archive_e001651~orig.jpg",
    "https://images-assets.nasa.gov/image/hubble-reveals-stellar-fireworks-in-skyrocket-galaxy_27946907106_o/hubble-reveals-stellar-fireworks-in-skyrocket-galaxy_27946907106_o~orig.jpg",
    "https://images-assets.nasa.gov/image/GSFC_20171208_Archive_e000144/GSFC_20171208_Archive_e000144~orig.jpg",
    "https://images-assets.nasa.gov/image/GSFC_20171208_Archive_e002070/GSFC_20171208_Archive_e002070~orig.jpg",
]

SAVE_DIR = "lensing/real_data/unlensed"

os.makedirs(SAVE_DIR, exist_ok=True)


for i, url in enumerate(URLS):

    print("Downloading:", url)

    r = requests.get(url)

    if r.status_code == 200:

        filename = f"galaxy_{i+1}.jpg"

        with open(os.path.join(SAVE_DIR, filename), "wb") as f:
            f.write(r.content)

        print("Saved", filename)

    else:
        print("Failed:", url)


print("Download complete ✅")
