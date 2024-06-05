import cv2
import matplotlib.pyplot as plt

# Example images for demonstration (replace with actual paths)
image_paths = ['frame_0001.png', 'frame_0002.png', 'frame_0003.png', 'frame_0004.png']
images = [cv2.imread(img) for img in image_paths]

# Create a montage of images
fig, axes = plt.subplots(1, len(images), figsize=(20, 5))
for ax, img in zip(axes, images):
    ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    ax.axis('off')

plt.savefig('dataset_samples.png')
plt.show()
