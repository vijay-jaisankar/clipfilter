## Case Study: on Synthetic black-and-white filter application

This directory contains additional material regarding how the case study was setup and run.

- **Dataset**: The datased used in this case study can be found on Huggingface [here](https://huggingface.co/datasets/vijay-jaisankar/clipfilter-case-study).
- Haversine distances were calculated in a similar manner to [applying conventional filters](../filter_application/README.md).
- The map visualisation was created in [map_visualusation_generation.ipynb](./map_visualusation_generation.ipynb). 
    - **Note**: To run this notebook,`geopandas` may need to be updated, which can be done by running the following command: ```pip install --upgrade geopandas```.


## Method of generating the dataset
To generate and apply these synthetic image filters, the [Qwen-Image-Edit-Fast Huggingface space](https://huggingface.co/spaces/multimodalart/Qwen-Image-Edit-Fast) was used. The prompt can be found in [PROMPT.txt](./PROMPT.txt).

## Qualitative Analysis

We qualitatively analyse the performance of GeoCLIP using path-occlusion blurring. [geoclip_qualitative_analysis.ipynb](./geoclip_qualitative_analysis.ipynb) contains more details on how the resulting heatmaps can be created and saved. The intention of this experiment is to explore this notion: *Can we find out the
image regions the model is most sensitive to, and can this help reveal
where and when the model goes wayward?*