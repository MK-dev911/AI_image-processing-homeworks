import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create a 500x500 image in BGR format
image = np.zeros((500, 500, 3), dtype=np.uint8)

# Define colors in BGR format
image[250:500, 0:250] = [0, 0, 255]  # Blue (BGR)
image[0:250, 250:500] = [0, 255, 0]  # Green (BGR)
image[0:250, 0:250] = [255, 0, 0]  # Red (BGR)
image[250:500, 250:500] = [0, 255, 255]  # Yellow (BGR)

# Convert BGR to RGB for display in Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.axis('off')
plt.show()
