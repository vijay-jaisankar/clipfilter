# CLIPFILTER


Code release for the paper **CLIPFILTER: Towards assessing Geolocation privacy risks of CLIP-based models for Social media users**, accepted to [ICVGIP 2026](https://icvgip.in/2026/).

# Abstract
Building on the impressive advancements in representation learning, foundation models like CLIP have been adapted for diverse
image understanding tasks. One such task is Image Geolocation,
which is the process of estimating the geographical coordinates of
the location where the image was captured. While it is a challenging
benchmark for image understanding, it presents significant privacy
risks for Social media users as it may facilitate unwanted tracking
and doxing. The objective of our study, **CLIPFILTER**, is to take
**a closer look at the performance of CLIP-based models on
Geolocation in realistic social media settings**. By contrasting
models’ performance on outdoor scenes and other images; and
examining the impact of applying commonly-used aesthetic image
filters, we present a realistic privacy risk assessment for CLIP-based
models for social media users. We then showcase how **black-and-
white filters can be good initial defenses for social media users**
and present a qualitative analysis of the spatial sensitivity of these
models under different filters. We finally highlight important future
research directions in this critical domain stemming from CLIPFILTER. Code and supplementary material for our work is released in this link: https://github.com/vijay-jaisankar/clipfilter.

---

# Code
Each subdirectory of this codebase contains nested READMEs with more information and instructions to set up and run experiments pertaining to CLIPFILTER.  
- To set up datasets and associated files, navigate to the  [data-preparation](./data-preparation/README.md) directory.
- To reproduce the results of/learn more about about the feasibility study on zero-shot city localisation, navigate to the [zero-shot-city-localisation](./zero-shot-city-localisation/README.md) directory.
- To reproduce the results of/learn more about benchmarking the effects of applying famous aesthetic social media filters on geolocation, navigate to the [filter-application](./filter-application/README.md) directory.
- To reproduce the results of/learn more about the case study on synthetic filter generation and application, and to visualise the results of our qualitative (patch-occlusion) analysis experiment, navigate to the [case-study](./case-study/README.md) directory.


# Acknowledgements and Contact Details
This project was done under the guidance of [Prof. Dinesh Babu Jayagopi](https://www.iiitb.ac.in/faculty/dinesh-babu-jayagopi).

Corresponding email: vijayjaisankar.vj@gmail.com

