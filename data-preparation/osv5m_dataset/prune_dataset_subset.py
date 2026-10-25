"""Prune the dataset based on the computed ZCore scores"""

import os
from argparse import ArgumentParser
from pathlib import Path
from shutil import copy2

import fiftyone as fo
import numpy as np
import torch
from tqdm import tqdm


def prune_and_save_dataset(
    zcore_scores_path: str,
    input_base_dir: str,
    output_dir: str,
    prune_rate: float = 0.80,
):
    """Perform pruning of the intermediate dataset based on a predefined Prune rate.

    Parameters
    ----------
    zcore_scores_path : str
        Absolute filepath to the computed Zcore npy file.
    input_base_dir : str
        Base directory where the Eurosat format dataset is stored.
    output_dir : str
        Desired output location of the converted dataset.
    prune_rate : float, optional
        Fraction of dataset to remove, by default 0.80
    """
    # Load ZCore numpy array
    score = np.load(zcore_scores_path)

    # Load FiftyOne dataset
    merged_path = os.path.join(input_base_dir, "eurosat10", "eurosat10", "train")
    train_data = fo.Dataset.from_dir(
        merged_path,
        dataset_type=fo.types.ImageClassificationDirectoryTree,
    )

    # Perform max-based pruning
    coreset_mask = np.argsort(score)[int(prune_rate * len(train_data)) :]
    coreset = torch.utils.data.Subset(train_data, coreset_mask)

    # Copy relevant images
    all_file_names = []
    selected_file_names = []
    for sample in train_data:
        all_file_names.append(sample.filepath)
    for idx in coreset_mask:
        selected_file_names.append(all_file_names[idx])

    os.makedirs(output_dir, exist_ok=True)

    for file_name in tqdm(selected_file_names):
        image_stem = Path(file_name).stem
        copy2(
            file_name,
            os.path.join(output_dir, f"{image_stem}.jpg"),
        )


if __name__ == "__main__":
    try:
        parser = ArgumentParser()
        parser.add_argument(
            "zcore_scores_path", type=str, help="Path to computed ZCore npy file"
        )
        parser.add_argument(
            "input_base_dir", type=str, help="Path to input Eurosat format dataset"
        )
        parser.add_argument("output_dir", type=str, help="Path to output Coreset")

        # Fix prune rate
        args = parser.parse_args()
        prune_and_save_dataset(
            zcore_scores_path=args.zcore_scores_path,
            input_base_dir=args.input_base_dir,
            output_dir=args.output_dir,
        )

    except Exception as e:
        print(f"Error while pruning the OSV-5M dataset: {e}")
