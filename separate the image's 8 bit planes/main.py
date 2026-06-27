import cv2
import numpy as np
import matplotlib.pyplot as plt

# خواندن تصویر به صورت خاکستری
image = cv2.imread('nature.jpg', cv2.IMREAD_GRAYSCALE)

bit_planes = []

# استخراج صفحات بیتی
for i in range(8): #برای هر بیت از 0 تا 7
    bit_plane = (image >> i) & 1 #استخراج بیت i
    bit_plane = bit_plane * 255 # تبدیل 0 و 1 به 0 و 255
    bit_planes.append(bit_plane)

# نمایش صفحات بیتی
fig, axes = plt.subplots(2, 4, figsize = (12, 6))

for i, ax in enumerate(axes.flat):
    ax.imshow(bit_planes[i], cmap='gray')
    ax.set_title(f"Bit Plane {i+1}")
    ax.axis('off')

plt.tight_layout()
plt.show()
