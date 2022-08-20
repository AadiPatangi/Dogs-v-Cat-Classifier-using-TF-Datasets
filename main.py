import keras
import tensorflow as tf 
import matplotlib.pyplot as plt
import cv2 as cv
from PIL import Image
import streamlit as st
import os
Work_Dir = "/Users/aadipatangi/Desktop/Python-Projects/Dogs v Cats Tensorflow/Dogs-v-Cat-Classifier-using-TF-Datasets/uploaded_images"
IMG_SIZE = 100
model = keras.models.load_model('/Users/aadipatangi/Desktop/Python-Projects/Dogs v Cats Tensorflow/Dogs-v-Cat-Classifier-using-TF-Datasets/content/saved_modelfinalz/my_model')


st.markdown("# [Dog or Cat](https://github.com/AadiPatangi/Dogs-v-Cat-Classifier-using-TF-Datasets)")
st.markdown("### **By: Aadi Patangi**")
image_file = st.file_uploader("Upload an image: ",type=["png","jpg","jpeg"])
