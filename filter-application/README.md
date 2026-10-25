## Filters' Application

This directory contains notebooks detailing how image filters' application experiments are run and results are gathered.

- [geoclip_filters_experiment.ipynb](./geoclip_filters_experiment.ipynb) and [osmclip_filters_experiments.ipynb](./osmclip_filters_experiments.ipynb) contain methods used to run CLIP-based models (`GeoCLIP` and `OSMCLIP`, respectively) to predict coordinates for images with various filters applied to them.
- [metrics_computation.ipynb](./metrics_computation.ipynb) contains methods used to compute and contrast Haversine distances, country and state level accuracies of the CLIP-based models across different filters.