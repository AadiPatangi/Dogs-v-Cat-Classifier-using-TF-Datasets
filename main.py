import keras
import tensorflow as tf 
import matplotlib.pyplot as plt
import cv2 as cv
from PIL import Image
model = keras.models.load_model('/Users/aadipatangi/Desktop/Python-Projects/Dogs v Cats Tensorflow/Dogs-v-Cat-Classifier-using-TF-Datasets/content/saved_modelfinalz/my_model')
print(model.summary(""))
