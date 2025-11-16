from skimage.filters import threshold_otsu
from skimage.filters import gaussian
from skimage.feature import canny
from skimage.morphology import dilation
from matplotlib import pyplot as plt
import numpy as np
import os
from PIL import Image
import cv2

'''
    Applies Otsu to all images in a directory. Need to specify input and output directories.
'''

def otsu_canny(image):
    #Otsu
    thresh = threshold_otsu(image)
    binary = image <= thresh

    #Canny
    edges = canny(binary)

    #Boolean to int
    binary = binary.astype(int)
    edges = edges.astype(int)

    #Dilate edges
    dilated_edges = dilation(edges)

    #Apply edges to otsu image
    binary[np.where(dilated_edges==1)] = 2

    return binary

input_dir = "" 
output_dir = ""

input_paths = sorted(os.listdir(input_dir))
length_paths = len(input_paths)

for i, path in enumerate(input_paths):
    # Read image
    image = plt.imread(os.path.join(input_dir, path))
    # Blur image
    blurred = gaussian(image, sigma=2)
    # Extract edges
    final = otsu_canny(blurred)
    # Save image
    output_path = os.path.join(output_dir, f"pretrain_{path}")
    cv2.imwrite(output_path, final)

    print(f"{i}/{length_paths} \t Image '{output_path}' saved")
