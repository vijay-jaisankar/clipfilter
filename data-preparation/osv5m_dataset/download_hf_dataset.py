"""Download test section of the OSV-5M Huggingface dataset into the current working directory"""

import os
import zipfile
from glob import glob

from huggingface_hub import hf_hub_download
from tqdm import tqdm

# Download all 5 test section zip files
for i in tqdm(range(5)):
    hf_hub_download(
        repo_id="osv5m/osv5m",
        filename=str(i).zfill(2) + ".zip",
        subfolder="images/test",
        repo_type="dataset",
        local_dir="datasets/OpenWorld",
    )
    hf_hub_download(
        repo_id="osv5m/osv5m",
        filename="README.md",
        repo_type="dataset",
        local_dir="datasets/OpenWorld",
    )

# Unzip the downloaded zip files
for root, dirs, files in os.walk("./datasets/OpenWorld/images/test"):
    for file in tqdm(files):
        if file.endswith(".zip"):
            with zipfile.ZipFile(os.path.join(root, file), "r") as zip_ref:
                zip_ref.extractall(root)
                os.remove(os.path.join(root, file))

# Download `test.csv`
hf_hub_download(
    repo_id="osv5m/osv5m",
    filename="test.csv",
    repo_type="dataset",
    local_dir="datasets/OpenWorld",
)

# Print statistics of images to verify download
base_images_path = "./datasets/OpenWorld/images/test"
for subdir in os.listdir(base_images_path):
    image_dir = os.path.join(base_images_path, subdir)
    print(f"Number of images in {subdir}: {len(glob(f'{image_dir}/*.jpg'))}")
