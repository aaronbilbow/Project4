
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
              -AbdomenCT (Folder) Contains 10000 different medical images of CT scan displaying an Abdomen <br>
              - BreastMRI (Folder) Contains 8954 different medical images of a Breast MRI <br>
              - CXR (Folder) Contains 10000 different medical images of an X-ray displaying a Chest <br>
              - ChestCT (Folder) Contains 10000 different medical images of CT scan displaying a Chest <br>
              - Hand (Folder) Contains 10000 different medical images of an X-ray displaying a Hand <br> 
              - HeadCT (Folder) Contains 10000 different medical images of CT scan displaying a Head<br>
              
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
The Dataset was then uploaded by each class into seperate folders to the GitHub Repository at the following website: [ https://github.com/aaronbilbow/Project4/tree/main/Images ] <br>
Table image showing what scans are contained in the data set: ![image](https://github.com/aaronbilbow/Project4/blob/main/Images/MRI_Table.png)<br>
__Dataset Limitations__<br>
- There are only 6 classes of scans that have been provided.<br>

## Results
The model was trained over 10 complete cycles and tested 1290 images each cycle.<br>
glorot_uniform had been used as it was introduced in a research paper in 2010. This was used as it attempts to<br> maintain roughly the same level of varience in the output
dataset as it had in the dataset input into the model. <br>

The following results where found when evaluating the model, it achieved an accuracy value of 0.9891% when<br>
prediciting which class an image, from one of the 6 relevant classes, belongs to. The validation accuracy for the model was 0.9909%. <br>

This can be highlighted through the graph below that was exported from the jupyter notebook located at [https://github.com/aaronbilbow/Project4/blob/main/project-4.ipynb]<br>
![image](https://github.com/aaronbilbow/Project4/blob/main/Images/Accuracy_Model.png)<br>

### Analysis and Future Questions
The loss at the start of the model starts off high before decreasing vastly and then contniuing to slowly decrease as the model is cycling through data points. <br>
With the accuracy increasing along with this it seems they are inversely proportional, this leads to the conclusion that the model is learning over time.<br>
A deeper intention behind this model is to put together a database of various scans with different health complications so that<br>
future models are able to predict/identify health problems earlier by scanning over the images and highlighting concerns as soon as possible.<br>
<br>




## Acknowledgements 
BibTeX
@misc{Medical MNIST Classification, author = {apolanco3225}, title = {Medical MNIST Classification}, year = {2017}, publisher = {GitHub}, journal = {GitHub repository}, howpublished = https://github.com/apolanco3225/Medical-MNIST-Classification}

License
Public Domain

Splash Image
Photo by Hush Naidoo on UnsplasheFa
