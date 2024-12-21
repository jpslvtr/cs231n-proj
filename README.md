# Ship Classification using Vision Transformers

This repository contains the paper and implementation details for our research on fine-tuning Vision Transformers (ViT) and Swin Transformers for ship classification.

## Overview

We investigate the effectiveness of Google's Vision Transformers (ViT) and Microsoft's Swin Transformers for classifying ships into five categories: cargo, military, carrier, cruise, and tankers. Our experiments demonstrate that fine-tuning significantly enhances classification accuracy, with ViT achieving 92.54% accuracy and Swin Transformer achieving 90.35% accuracy on the test set.

## Dataset

* 8,908 total ship images from Analytics Vidhya hackathon (2019)
* 6,252 labeled images used for experiments  
* Five ship categories: cargo, military, carrier, cruise, and tankers
* Images resized to 224x224 pixels

## Models

* Vision Transformer (ViT): `google/vit-base-patch16-224-in21k`
* Swin Transformer: `microsoft/swin-tiny-patch4-window7-224`

## Key Results

* ViT best accuracy: 92.54% (learning rate: 5e-5)
* Swin Transformer best accuracy: 90.35% (learning rate: 3e-3) 
* Baseline accuracies before fine-tuning:
 * ViT: 2.99%
 * Swin: 4.10%

## Acknowledgements

* Analytics Vidhya for the dataset
* Hugging Face Transformers library
* Vision Transformer (ViT) from Google Research  
* Swin Transformer from Microsoft Research

## Citation

If you use this work in your research, please cite:

```bibtex
@article{park2024comparative,
 title={Comparative Analysis of Fine-Tuning Approaches for Ship Classification Using Transformers},
 author={Park, James and Laguerre, Jean},
 institution={Stanford University},
 year={2024}
}