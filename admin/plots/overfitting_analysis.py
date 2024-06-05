import matplotlib.pyplot as plt

# Example loss values based on your project
epochs = range(1, 16)
training_loss = [0.8, 0.6, 0.5, 0.4, 0.35, 0.3, 0.28, 0.26, 0.24, 0.22, 0.21, 0.2, 0.18, 0.16, 0.15]
validation_loss = [0.9, 0.75, 0.65, 0.6, 0.55, 0.52, 0.5, 0.49, 0.47, 0.46, 0.44, 0.43, 0.42, 0.41, 0.4]

plt.figure(figsize=(10, 6))
plt.plot(epochs, training_loss, 'r', label='Training loss')
plt.plot(epochs, validation_loss, 'b', label='Validation loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.ylim(0, 1)  # Adjust y-axis scale
plt.legend()
plt.grid(True)
plt.savefig('overfitting_analysis.png')
plt.show()
