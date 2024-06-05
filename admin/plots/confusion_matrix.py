import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Example true labels and predictions for demonstration
true_labels = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]
predictions = [0, 1, 1, 0, 0, 2, 0, 2, 2, 0, 1, 2, 0, 1, 1]

# Generate the confusion matrix
cm = confusion_matrix(true_labels, predictions)
class_names = ['Class 0', 'Class 1', 'Class 2']  # Add class names

# Plot the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.savefig('confusion_matrix.png')
plt.show()
