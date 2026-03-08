import cv2
from modules.preprocessing import to_grayscale, add_noise, denoise, enhance_contrast, detect_edges
from modules.visualization import show_pipeline

# Load single image
image = cv2.imread('assets/xray.jpg')

# Pipeline
gray = to_grayscale(image)
noisy = add_noise(gray)
blur = denoise(noisy)
enhanced = enhance_contrast(blur)
edges = detect_edges(enhanced)

# Display results
titles = ['Raw Image', 'Noisy Image', 'Noise Reduced', 'Contrast Enhanced', 'Edge Detection']
images = [gray, noisy, blur, enhanced, edges]

show_pipeline(images, titles)
