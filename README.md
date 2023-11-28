#### Overview

Built a model to classify MRI images of the human head as having a specified type of tumor or not. The 4 classes are; "Meningioma", "Glioma", "Pituitary" and "No tumor". The dataset is obtained from kaggle [Brain Tumor MRI Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset). The data is made up of four directories for the four classes.


#### Model

Image preprocessing via flipping, rescaling, normalising, zooming and rotation is applied to the train set only. The Resnet50 and efficientnet pretrained model is used for training, the last layer is changed to reflect the number of classes.
The model has two versions due to the different pretrained layers used.
The accuracy of training and testing sets for version 2 after 15 epochs is 98.9% and 98.1% respectively with losses of 0.031 and 0.083. Version 2 after 25 epochs of training had 87.3% and 90.1% accuracy and losses of 0.3435 and 0.2842 for both the training and testing sets respectively.

##### Version 3 to be updated to correctly add the classes.