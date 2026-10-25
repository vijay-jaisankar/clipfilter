"""Convert OSV-5M dataset into EuroSAT-10 format for compatibility with ZCore"""

import os
from argparse import ArgumentParser
from glob import glob
from pathlib import Path
from shutil import copy2

import pandas as pd
from tqdm import tqdm


def filter_countries_and_convert_eurosat(
    output_base_dir: str, list_accepted_countries: list = ["US", "IN", "BR"]
):
    """Filter images based on their country codes, and convert the corresponding test section into the EuroSAT-10 format.

    Parameters
    ----------
    output_base_dir : str
        Desired output location of the converted dataset.
    list_accepted_countries : list, optional
        List of country codes to be used in analysis, by default ['US', 'IN', 'BR']
    """
    # @note We assume the OSV-5M dataset has already been downloaded in the current working directory.
    df = pd.read_csv("./datasets/OpenWorld/test.csv")

    # Store mapping between ID and country code
    image_mapping = {}
    for i in tqdm(range(len(df))):
        row = df.iloc[i]
        _id = row["id"]
        lat = row["latitude"]
        lon = row["longitude"]
        country = row["country"]
        # Look for whitelisted countries
        if country in list_accepted_countries:
            image_mapping[_id] = f"{country}_{lat}_{lon}"

    # Create output directories
    os.makedirs(os.path.join(output_base_dir, "eurosat10"), exist_ok=True)
    os.makedirs(os.path.join(output_base_dir, "eurosat10", "eurosat10"), exist_ok=True)
    os.makedirs(
        os.path.join(output_base_dir, "eurosat10", "eurosat10", "train"), exist_ok=True
    )

    # Create output subdirectories for each country code
    base_output_dir = os.path.join(output_base_dir, "eurosat10", "eurosat10", "train")
    for _code in list_accepted_countries:
        os.makedirs(os.path.join(base_output_dir, _code), exist_ok=True)

    # Load base image path @todo: Error handling
    base_images_path = "./datasets/OpenWorld/images/test"

    # Process whitelisted images
    for subdir in os.listdir(base_images_path):
        print(f"Processing {subdir}...")
        image_dir = os.path.join(base_images_path, subdir)
        input_images = glob(f"{image_dir}/*.jpg")
        for input_image in tqdm(input_images):
            _id = Path(input_image).stem
            id_int = int(_id)
            if id_int in image_mapping:
                descriptor = image_mapping[id_int]
                country_code = descriptor.split("_")[0]
                lat = descriptor.split("_")[1]
                lon = descriptor.split("_")[2]
                output_path = os.path.join(
                    base_output_dir, country_code, f"{_id}_{lat}_{lon}.jpg"
                )
                copy2(input_image, output_path)


if __name__ == "__main__":
    try:
        parser = ArgumentParser()
        parser.add_argument(
            "output_base_dir", type=str, help="Path to output full EuroSAT dataset"
        )
        # Fix whitelisted countries per city
        args = parser.parse_args()
        filter_countries_and_convert_eurosat(
            output_base_dir=args.output_base_dir,
        )
    except Exception as e:
        print(f"Error while processing the OSV-5M dataset: {e}")
