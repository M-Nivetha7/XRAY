"""
Modules package for X-ray Processing Project.

This package contains:
- preprocessing: functions for grayscale conversion, noise addition, denoising, contrast enhancement, and edge detection
- visualization: helper functions for displaying image pipelines
"""

# Import functions from preprocessing
from .preprocessing import (
    to_grayscale,
    add_noise,
    denoise,
    enhance_contrast,
    detect_edges,
)

# Import visualization helpers
from .visualization import (
    show_pipeline,
)

# Define what gets exported when you do: from modules import *
__all__ = [
    "to_grayscale",
    "add_noise",
    "denoise",
    "enhance_contrast",
    "detect_edges",
    "show_pipeline",
]
