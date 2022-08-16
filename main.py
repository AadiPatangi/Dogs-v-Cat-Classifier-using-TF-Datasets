import tensorflow as tf


model = tf.keras.models.load_model('/workspaces/Dogs-v-Cat-Classifier-using-TF-Datasets/content/saved_modelfinal/my_model')
print(model.summary())