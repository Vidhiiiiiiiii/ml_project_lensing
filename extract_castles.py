import tarfile

FILE = "castles-fits.tar.gz"   # change name if needed
OUTPUT = "castles_extracted"

with tarfile.open(FILE, "r:gz") as tar:
    tar.extractall(OUTPUT)

print("Extraction complete ✅")
