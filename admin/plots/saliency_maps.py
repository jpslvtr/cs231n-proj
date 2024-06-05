import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load a pre-trained model
model = models.resnet18(pretrained=True)
model.eval()

# Function to preprocess the image
def preprocess_image(img_path):
    input_image = Image.open(img_path).convert('RGB')
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)
    return input_batch

# Function to generate a saliency map
def generate_saliency_map(model, input_batch):
    input_batch.requires_grad_()
    output = model(input_batch)
    output_idx = output.argmax()
    output_max = output[0, output_idx]
    output_max.backward()
    saliency, _ = torch.max(input_batch.grad.data.abs(), dim=1)
    saliency = saliency[0].cpu().numpy()
    return saliency

# Path to the input image
image_path = 'frame_0050.png'

# Preprocess the image
input_batch = preprocess_image(image_path)

# Generate the saliency map
saliency_map = generate_saliency_map(model, input_batch)

# Normalize the saliency map for better visualization
saliency_map = (saliency_map - saliency_map.min()) / (saliency_map.max() - saliency_map.min())

# Apply a color map for better visualization
saliency_map_colored = cv2.applyColorMap(np.uint8(255 * saliency_map), cv2.COLORMAP_JET)

# Load the original image for display
image = cv2.imread(image_path)

# Resize saliency map to match the original image size
saliency_map_resized = cv2.resize(saliency_map_colored, (image.shape[1], image.shape[0]))

# Overlay the saliency map on the original image
overlay = cv2.addWeighted(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), 0.6, saliency_map_resized, 0.4, 0)

# Create a visualization of the saliency map
fig, ax = plt.subplots(1, 3, figsize=(18, 6))

# Display the original image
ax[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
ax[0].set_title('Original Image')
ax[0].axis('off')

# Display the saliency map
ax[1].imshow(saliency_map_resized)
ax[1].set_title('Saliency Map')
ax[1].axis('off')

# Display the overlay
ax[2].imshow(overlay)
ax[2].set_title('Overlay')
ax[2].axis('off')

# Save the visualization as an image file
plt.savefig('improved_saliency_maps.png')
plt.show()
