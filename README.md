# Thesis Shyrano Karia: Using Degradation Representation Learning For Super-Resolving Face Images
Most of the code used in this thesis was conducted from another Github repository: https://github.com/The-Learning-And-Vision-Atelier-LAVA/DASR. A few modifications to this code have been done. 

## Required packages
- Python, version 3.7.9
- CUDA, version 10.0
- PyTorch, version 1.1.0
- Numpy
- Scikit image
- Imageio
- Matplotlib
- OpenCV

The code is seperated in two subfolders: one for the DASR model (folder name: DASR) and none for the model without DRL (folder name: Without DRL).

## Train
### 1. Prepare training data 

Download the [SiblingsDB](https://areeweb.polito.it/ricerca/cgvg/siblingsDB.html) dataset and save the dataset in `your_data_path/DF2K/HR`.

### 2. Begin to train
Run `./main.sh` to train on the SiblingsDB dataset. Update `dir_data` in the bash file as `your_data_path`.

## Test
### 1. Prepare test data 

1.1 Download [real-human dataset](https://www.kaggle.com/datasets/hamzaboulahia/hardfakevsrealfaces) in `your_data_path/benchmark`.

1.2 Run `imageformat.ipynb` to make sure the images are formatted to .png files.

1.3 Download [UTKFace](https://www.kaggle.com/datasets/jangedoo/utkface-new) in another data path then `your_data_path/benchmark`.

1.4 Change current directory in `imageformat.ipynb` to the one generated in 1.3 and run`imageformat.ipynb`, to make sure the images are formatted to .png files.

1.5 Delete the following images from the [UTKFace](https://www.kaggle.com/datasets/jangedoo/utkface-new) dataset: 55_0_0_20170113184836584, 65_0_0_20170113190804729, 29_0_0_20170113210605445, 
, 32_0_0_20170113210127524, 32_1_0_20170113210605443, 35_0_0_20170113210127529, 38_0_0_20170117140605859, 35_0_1_20170117143158631 & 26_1_1_20170116232657066

1.6 Run categorize.py, to make subdirectories from the [UTKFace](https://www.kaggle.com/datasets/jangedoo/utkface-new) dataset.

### 2. Begin to test

2.1 Run `./test.sh` to test on real-human dataset. Update `dir_data` in the bash file as `your_data_path`.

2.2 Remove the real-human dataset from `your_data_path/benchmark`.

2.4 Copy files in folders for each class via the terminal. For example to copy all females in a new created folder: cp ../UTK/female/*/*/* ../females. Then move the files from the 'females' folder to `your_data_path/benchmark`.

2.5 Run `./test.sh` to test on UTKFace dataset. Update `dir_data` in the bash file as `your_data_path`

## Acknowledgements
This code is built on [DASR](https://github.com/The-Learning-And-Vision-Atelier-LAVA/DASR), [EDSR (PyTorch)](https://github.com/thstkdgus35/EDSR-PyTorch), [IKC](https://github.com/yuanjunchai/IKC) and [MoCo](https://github.com/facebookresearch/moco). I would like to thank the authors for sharing their code. 

