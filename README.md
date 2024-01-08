
# Project4
![image](https://github.com/aaronbilbow/Project4/blob/main/Images/MRI_Machine.jpg)

Project4 - UWA/edX Data Analytics Bootcamp

GitHub repository can be located at: [https://github.com/aaronbilbow/Project4.git](https://github.com/aaronbilbow/Project4.git)

Presentation website can located at: [Project4](https://github.com/aaronbilbow/Project4/blob/main/html.html)

## Table of Contents
1. [Introduction](https://github.com/aaronbilbow/Project4#introduction)
    1. [Repository Structure](https://github.com/aaronbilbow/Project4#repository-structure)
    2. [Requirements](https://github.com/aaronbilbow/Project4#requirements)
    3. [Dataset](https://github.com/aaronbilbow/Project4#dataset)
2. [Results](https://github.com/aaronbilbow/Project4#results)
    1. [Analysis and Future Questions](https://github.com/aaronbilbow/Project4#analysis-and-future-questions)
3. [Acknowledgements](https://github.com/aaronbilbow/Project4#acknowledgements)

## Introduction
The project will create a predictive model of an MRI/CT Scan from one of 6 classes. The project is based on a MNIST data set was put together by BibTeX in 2017 and contains medical images that are 64x64.<br>
There are 58954 medical images that belong to 6 different classes that have been provided for this model to be trained on.<br>
These images where orginally taken from various other data sets and converted into the 64x64 style. <br>


### Repository Structure
The root directory contains:<br>
              -app.py<br>
              -README.md<br>
              -project-4.ipynb<br>
              
Other directories:<br>
Images(Folder)<br>
              - Contains the image used in the README.<br>
              -AbdomenCT (Folder) Contains 10000 different medical images of CT scan displaying an Abdomen in a 64x64 style <br>
              - BreastMRI (Folder) Contains 8954 different medical images of a Breast MRI displayed in a 64x64 style <br>
              - CXR (Folder) Contains 10000 different medical images of an X-ray displaying a Chest in a 64x64 style <br>
              - ChestCT (Folder) Contains 10000 different medical images of CT scan displaying a Chest in a 64x64 style <br>
              - Hand (Folder) Contains 10000 different medical images of an X-ray displaying a Hand in a 64x64 style <br> 
              - HeadCT (Folder) Contains 10000 different medical images of CT scan displaying a Head in a 64x64 style <br>
              
Admin(Folder)<br>
              -'workinglog.txt'<br>
              -'medical.txt'<br> 
              -'Project4.docx'<br>

### Requirements
pathlib<br>
numpy<br>
matplotlib<br>
sklearn<br>
tensorflow <br>
streamlit<br>
Pillow<br>

### Dataset
Retrieved data from the following website: https://www.kaggle.com/datasets/andrewmvd/medical-mnist <br>
The Dataset was then uploaded by each class into seperate folders to the GitHub Repository at the following website: [ https://github.com/aaronbilbow/Project4/tree/main/Images ] 
Table image showing what scans are contained in the data set: ![image](https://github.com/aaronbilbow/Project4/blob/main/Images/MRI_Table.png)
__Dataset Limitations__
- There are only 6 classes of scans that have been provided.

## Results
###### The model achieves x precision, and x accuracy when prediciting which class an image, from one of the 6 relevant classes, belongs to. 

### Analysis and Future Questions
A deeper intention behind this model is to put together a database of various scans with different health complications so that<br>
future models are able to predict/identify health problems earlier by scanning over the images and highlighting possible concerns.<br> </p>
## Acknowledgements 
BibTeX
@misc{Medical MNIST Classification, author = {apolanco3225}, title = {Medical MNIST Classification}, year = {2017}, publisher = {GitHub}, journal = {GitHub repository}, howpublished = https://github.com/apolanco3225/Medical-MNIST-Classification

License
Public Domain

Splash Image
Photo by Hush Naidoo on UnsplasheFa
