"""Generate random subset of images sampled from each city in the Instacities dataset"""

import os
import random
from argparse import ArgumentParser
from glob import glob
from pathlib import Path
from shutil import copy2

from tqdm import tqdm

# Set random seed
random.seed(42)


def select_random_subset(
    input_images_base_dir: str, output_base_dir: str, num_files_to_select=1000
):
    """Select random subset of images from the Instacities dataset.

    Parameters
    ----------
    input_images_base_dir: str
        Parent directory of the Instacities images dataset, should contain 10 subdirectories.
    output_base_dir: str
        Desired output location of the filtered subset.
    num_files_to_select : int, optional
        Number of images to select per city, by default 1000
    """
    # Create one output directory for each city
    subfolders = [
        Path(f.path).stem for f in os.scandir(input_images_base_dir) if f.is_dir()
    ]
    os.makedirs(output_base_dir, exist_ok=True)

    for city_name in subfolders:
        os.makedirs(os.path.join(output_base_dir, city_name), exist_ok=True)

    # Process each city
    for city_name in subfolders:
        print(f"Processing city: {city_name}")
        input_dir = os.path.join(input_images_base_dir, city_name)
        all_files = glob(f"{input_dir}/*.jpg")
        input_images = random.sample(all_files, num_files_to_select)

        # Copy files
        output_dir = os.path.join(output_base_dir, city_name)
        for input_image in tqdm(input_images):
            stem = Path(input_image).stem
            output_path = os.path.join(output_dir, f"{stem}.jpg")
            copy2(input_image, output_path)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "input_images_base_dir", type=str, help="Path to Instacities images dataset"
    )
    parser.add_argument(
        "output_base_dir", type=str, help="Path to output filtered subset"
    )
    # Fix 1000 images per city
    args = parser.parse_args()
    select_random_subset(
        input_images_base_dir=args.input_images_base_dir,
        output_base_dir=args.output_base_dir,
    )
