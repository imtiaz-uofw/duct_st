# Detection of Spatial Domain and Benchmarking the Domain Using Human Breast Cancer Ductal Carcinoma in Situ
## Overview
Six different spatial transcriptomic clustering algorithms are adopted in this project to find out the spatial domain of the Ductal Carcinoma in Situ data. Based on the spatial domain cluster group, the marker genes were identified per each cluster group. After that, the cell groups for each of the cluster groups were identified based on the top marker genes to benchmark the algorithms.

<p align="center">
	<img src="https://github.com/imtiaz-uofw/test/blob/main/stdiagram.png?raw=true" width="367.9" height="622.7" alt="Image">
</p>


## Folder hierarchy
#### The 10x genomic's Ductal carcinoma is Situ Data is chosen. After grabbing the source codes, you can see the folder hierarchy as follows:
```
.
├── data
│   ├── spatial
│   │   └── aligned_fiducials.jpg
│   │   └── detected_tissue_image.jpg
│   │   └── scalefactors_json.json
│   │   └── tissue_hires_image.png
│   │   └── tissue_lowres_image.png
│   │   └── tissue_positions_list.csv
│   ├── filtered_feature_bc_matrix.h5
│   ├── raw_feature_bc_matrix.h5
├── preprocessing
│   └── data_importing_and_annoting.py
│   └── lib_installation.py
│   └── preprocessing.py
├── spatial domain
│   └── h_clust.py
│   └── k_means.py
│   └── leiden.py
│   └── louvain.py
│   └── spagcn.py
│   └── squidpy.py
├── tutorial
│   └── tutorial.ipynb
│   └── tutorial.py
└── readme.md
```
## Python Platform
#### Recommended Platform
```
Google Colaboratory
Pycharm
Jupyter notebook
```
## Required Installation to Run the Code
```
# Configuring the virtual environment
Python: 3.8.8
Python packages: pandas = 1.2.4, numpy = 1.19.1, python-igraph=0.9.1, scipy = 1.6.3, scanpy = 1.7.2, anndata = 0.7.6, natsort = 7.1.1, sklearn = 0.24.2
```
## Code Running Instruction
#### Steps for running the packages
```
1. load or choose folder for data
1. lib_installation.py
2. data_importing_and_annoting.py
3. preprocessing.py
4. leiden.py
5. louvain.py
6. k_means.py
7. h_clust.py
8. squidpy.py
9. spagcn.py
```
## Tutorial
#### To run the ipynb file
```
jupyter nbconvert --to python nb.ipynb tutorial.ipynb
upload to colabratory and run tutorial.ipynb 
```
## Download data
|      Platform      |       Tissue     |    SampleID   |
|:----------------:|:----------------:|:------------:|
| [10x Visium](https://support.10xgenomics.com) | Human breast cancer| [Ductal Carcinoma In Situ & Invasive Carcinoma](https://www.10xgenomics.com/resources/datasets/human-breast-cancer-ductal-carcinoma-in-situ-invasive-carcinoma-ffpe-1-standard-1-3-0) 

## Usage
With this project one can do the following
• Finding out the spatial domain from spatial transcriptomics.
• How to use or run different spatial transcriptomic algorithms. 
• Finding the top marker genes through.
• Cell annotation of the marker genes.
• Benchmarking spatial domain clustering based on the cell.
• Helping biomarkers to find out the genes that belongs to ductal cell.

## Contact
Feel free to submit an issue or contact me at ahmed-m70@webmail.uwinnipeg.ca for problems about the packages.
