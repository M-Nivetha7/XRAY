import streamlit as st
import cv2
import numpy as np
from modules.preprocessing import to_grayscale, add_noise, denoise, enhance_contrast, detect_edges

st.title("🩻 X-ray Image Processing Web App")

# File uploader
uploaded_file = st.file_uploader("Upload an X-ray image", type=["jpg","jpeg","png"])

if uploaded_file is not None:
    # Read uploaded image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Interactive parameters
    noise_std = st.slider("Noise Standard Deviation", 0, 50, 15)
    kernel_size = st.slider("Gaussian Blur Kernel Size", 3, 11, 5, step=2)
    clip_limit = st.slider("CLAHE Clip Limit", 1.0, 5.0, 2.0)
    low_thresh = st.slider("Canny Low Threshold", 0, 100, 50)
    high_thresh = st.slider("Canny High Threshold", 100, 300, 150)

    # Pipeline
    gray = to_grayscale(image)
    noisy = add_noise(gray, std=noise_std)
    blur = denoise(noisy, kernel_size=kernel_size)
    enhanced = enhance_contrast(blur, clip=clip_limit)
    edges = detect_edges(enhanced, low=low_thresh, high=high_thresh)

    # Display results in full width
    titles = ['Raw Image', 'Noisy Image', 'Noise Reduced', 'Contrast Enhanced', 'Edge Detection']
    images = [gray, noisy, blur, enhanced, edges]

    st.subheader("Processing Results")
    for i in range(len(images)):
        st.image(images[i], caption=titles[i], use_column_width=True, channels="GRAY")
