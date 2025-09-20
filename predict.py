import tensorflow as tf
from tensorflow import keras
from keras._tf_keras.keras.preprocessing.image import img_to_array, load_img
from keras._tf_keras.keras.models import load_model

import numpy as np

model = load_model('parkinson_model.h5')

def predict_parkinson(image_path):
   
    image = load_img(image_path, target_size=(128, 128))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0

    prediction = model.predict(image)
    if prediction[0][0] >= 0.5:
        print("Prediction result: Parkinson Detected")
        return "Parkinson Detected"
    else:
        print("Prediction result: Healthy")
        return "Healthy"
