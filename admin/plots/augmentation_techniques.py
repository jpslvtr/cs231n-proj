import cv2
import matplotlib.pyplot as plt
import numpy as np

# Example image for demonstration (replace with actual path)
image = cv2.imread('frame_0050.png')

# Apply different augmentation techniques
height, width = image.shape[:2]
cropped = image[height//4:3*height//4, width//4:3*width//4]  # Adjusted cropping
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
bright = cv2.convertScaleAbs(image, alpha=1.5, beta=30)  # Brightened image
noise = np.random.normal(0, 25, image.shape).astype(np.uint8)
noisy = cv2.add(image, noise)

# Create a montage of augmented images
images = [image, cropped, rotated, bright, noisy]
titles = ['Original', 'Cropped', 'Rotated', 'Bright', 'Noisy']

fig, axes = plt.subplots(1, len(images), figsize=(20, 5))
for ax, img, title in zip(axes, images, titles):
    ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    ax.set_title(title)
    ax.axis('off')

plt.savefig('augmentation_techniques.png')
plt.show()
