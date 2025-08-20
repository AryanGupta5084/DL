import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model

# Load model
model = load_model("trained_model.h5")

st.title("👤 Gender Classification from Fingerprint")

uploaded_file = st.file_uploader("Upload a fingerprint image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)
    img_resized = cv2.resize(img, (96, 96)).reshape(1,96,96,1) / 255.0

    st.image(img, caption="Uploaded Fingerprint", use_column_width=True)

    prediction = model.predict(img_resized)
    label = "Male" if np.argmax(prediction) == 0 else "Female"

    st.success(f"Predicted Gender: {label}")
