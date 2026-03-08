import cv2
import numpy as np

def to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def add_noise(gray, mean=0, std=15):
    noise = np.random.normal(mean, std, gray.shape)
    noisy_image = np.clip(gray + noise, 0, 255).astype(np.uint8)
    return noisy_image

def denoise(image, kernel_size=5):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

def enhance_contrast(image, clip=2.0, grid=(8,8)):
    clahe = cv2.createCLAHE(clipLimit=clip, tileGridSize=grid)
    return clahe.apply(image)

def detect_edges(image, low=50, high=150):
    return cv2.Canny(image, low, high)
