# Instacities dataset processing

We select a random subset of the [InstaCities1M](https://gombru.github.io/2018/08/01/InstaCities1M/) dataset to assess the feasibility of CLIP models in zero-shot city localisation. 

1. First, download the Instacities1M Dataset from the [Project Page](https://gombru.github.io/2018/08/01/InstaCities1M/). **Note**: While running the experiments of CLIPFILTER, we used the given [CVC Lab download link](http://datasets.cvc.uab.es/InstaCities1M/InstaCities1M.zip).
2. After downloading and unzipping the dataset, you should have `captions_resized_1M`, `img_resized_1M`, and `InstaCities1M_readme.txt`. We denote the absolute path of `./img_resized_1M/cities_instagram/` (which should contain 10 subfolders, each containing `.jpg`) images as `input_images_dir`.
3. Create a new directory to store the outputs using `mkdir -p ./outputs`.
4. Run ```python generate_random_subset.py $input_images_dir ./outputs``` to populate the chosen images into `./outputs`.