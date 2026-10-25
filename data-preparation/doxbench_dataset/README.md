# DoxBench dataset processing

We select the [DoxBench](https://huggingface.co/datasets/MomoUchi/DoxBench) dataset to incorporate more aspects of privacy analysis in social media
settings. As there is no defined train and test set, we use all images in the Huggingface release.

1. First, create a Huggingface user token using [these instructions](https://huggingface.co/docs/hub/en/security-tokens). This token will be used to download the dataset locally. Then, install the Huggingface CLI using [these insructions](https://huggingface.co/docs/huggingface_hub/en/guides/cli) authenticate your account by running this command in the terminal: `hf auth login --token <YOUR-CREATED-TOKEN>`
2. Run ```python download_doxbench_dataset.py``` that downloads the DoxBench dataset. Please note that this script can take a moderate amount of time. After this step, you should have a directory with the path `./doxbench_dataset`.
3. Create a new parent directory to store the images using `mkdir -p doxbench_image_filter_dataset`.
8. Next, install [PILGram](https://github.com/akiomik/pilgram) using ```pip install pilgram```. Finally, run ```python apply_instagram_filters.py ./input_images_directory ./doxbench_image_filter_dataset``` to populate `./doxbench_image_filter_dataset` with 7 subfolders - `original`, `clarendon`, `gingham`, `willow`, `inkwell`, `lark`, and `moon`. This dataset forms the basis for the experiments analysing the effects on applying aesthetic filters geolocation performance.