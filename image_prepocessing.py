import numpy as np
import nibabel as nib
import cv2
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from keras.applications.resnet50 import ResNet50, preprocess_input
from keras.preprocessing.image import img_to_array
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the ABIDE phenotypic CSV file
df = pd.read_csv("Phenotypic_V1_0b.csv")

# Show the first few rows
print(df[['SITE_ID', 'SUB_ID', 'DX_GROUP', 'AGE_AT_SCAN']].head())

asd_subjects= df[df['DX_GROUP'] == 1]
print (asd_subjects[['SITE_ID', 'SUB_ID']].head())

mri_path = "0154423_struc_CM.mat.gz"
img  = nib.load(mri_path)
img_data = img.get_fdata()

print("MRI data shape:", img_data.shape)

print("Environment setup complete.")
# def load_nifti_image(file_path):
#     """Load a NIfTI image file."""
#     img = nib.load(file_path)
#     return img.get_fdata()