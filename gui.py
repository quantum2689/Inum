import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

model = tf.keras.models.load_model('model.h5')

def preprocess_image(uploaded_file):
    img = Image.open(uploaded_file).convert('L')  # Convert to grayscale
    img = img.resize((28, 28))  # Resize to 28x28 pixels
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = img_array / 255.0  # Normalize to [0, 1]
    return img_array

st.title("Inum")

img = st.file_uploader("uplode your img...",type=["png", "jpg", "jpeg"])

if img is not None:
    img_array = preprocess_image(img)

    predictions = model.predict(img_array)

    predicted_class = np.argmax(predictions)

    st.write(f'Predicted Class: {predicted_class}')
    st.image(img, caption=f'Uploaded Image', use_column_width=True)
else:
    st.write("no file is uploded...")
