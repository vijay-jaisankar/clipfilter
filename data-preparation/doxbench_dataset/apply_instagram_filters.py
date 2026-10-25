"""Use PILGram to apply Instagram filters to a set of images."""

import os
from argparse import ArgumentParser
from glob import glob
from pathlib import Path

import pilgram
from PIL import Image
from tqdm import tqdm


def apply_instagram_filters(
    input_images_dir: str,
    output_base_dir: str,
    list_filters=[
        "original",
        "clarendon",
        "willow",
        "inkwell",
        "gingham",
        "lark",
        "moon",
    ],
):
    """Apply and save Instagram filters applied individually to images.

    Parameters
    ----------
    input_images_dir : str
        Path to directory containing input images.
    output_base_dir : str
        Desired output location of the consolidated dataset.
    list_filters : list, optional
        List of filters to be applied, by default ["original", "clarendon", "willow", "inkwell", "gingham", "lark", "moon"]
    """
    # Create output directories
    os.makedirs(output_base_dir, exist_ok=True)
    for filter_name in list_filters:
        os.makedirs(os.path.join(output_base_dir, filter_name), exist_ok=True)

    # Process images
    all_input_images = glob(
        f"{input_images_dir}/*.jpg"
    )  # @todo support more image types
    for filter_name in list_filters:
        print(f"Applying {filter_name} filter...")
        for input_image in tqdm(all_input_images):
            # Load original image
            image_stem = Path(input_image).stem
            im = Image.open(input_image).convert("RGB")

            # Set output path
            output_path = os.path.join(
                output_base_dir,
                filter_name,
                f"{image_stem}_{filter_name}.jpg",
            )

            # Apply filer
            if filter_name == "original":
                im.save(output_path)
            elif filter_name == "clarendon":
                pilgram.clarendon(im).save(output_path)
            elif filter_name == "gingham":
                pilgram.gingham(im).save(output_path)
            elif filter_name == "willow":
                pilgram.willow(im).save(output_path)
            elif filter_name == "inkwell":
                pilgram.inkwell(im).save(output_path)
            elif filter_name == "lark":
                pilgram.lark(im).save(output_path)
            elif filter_name == "moon":
                pilgram.moon(im).save(output_path)
            else:
                print("Invalid method supplied.")


if __name__ == "__main__":
    try:
        parser = ArgumentParser()
        parser.add_argument(
            "input_images_dir",
            type=str,
            help="Path to directory containing input images",
        )
        parser.add_argument(
            "output_base_dir",
            type=str,
            help="Path to output directory for filtered images",
        )
        # Fix filters to be applied
        args = parser.parse_args()
        apply_instagram_filters(
            input_images_dir=args.input_images_dir,
            output_base_dir=args.output_base_dir,
        )
    except Exception as e:
        print(f"Error while applying filters: {e}")
