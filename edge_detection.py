# Edge detection in Python
import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = 'my_img.png'
min_val = 100
max_val = 200
kernel_size = 3

image = cv2.imread(image_path, 0)
image_edges = cv2.Canny(image, min_val, max_val, kernel_size)

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Image before edge detection'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges, cmap = 'gray')
plt.title('Image after edge detection'), plt.xticks([]), plt.yticks([])

plt.show()