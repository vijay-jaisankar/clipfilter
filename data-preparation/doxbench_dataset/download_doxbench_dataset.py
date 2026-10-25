"""Download the DoxBench datsaet Huggingface dataset into a subfolder in the current working directory"""

import os
import zipfile
from glob import glob

import pandas as pd
from huggingface_hub import hf_hub_download
from tqdm import tqdm

# Note: First, run hf auth login --token <YOUR-HF-TOKEN>

# Create the output directory
local_dir = "./doxbench_dataset"
os.makedirs(local_dir, exist_ok=True)

# Download the images and labels
snapshot_download(repo_id="MomoUchi/DoxBench", local_dir=local_dir, repo_type="dataset")

# Print a sample of the dataset summary to verify download
results_csv_path = os.path.join(local_dir, "result.csv")
df = pd.read_csv(results_csv_path)
print(f"Dataset summary sample:")
print(df.head())
