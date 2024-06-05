import os
from PIL import Image
import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim
import lpips

def calculate_metrics(ground_truth, predicted):
    psnr_value = psnr(np.array(ground_truth), np.array(predicted))
    ssim_value = ssim(np.array(ground_truth), np.array(predicted), multichannel=True)
    lpips_model = lpips.LPIPS(net='alex')
    lpips_value = lpips_model(ground_truth, predicted).item()
    return psnr_value, ssim_value, lpips_value

def evaluate_scene(scene_num):
    base_path = f"data/results/scene{scene_num}"
    ground_truth_folder = os.path.join(base_path, "ground_truth")
    predicted_folder = os.path.join(base_path, "predicted")

    ground_truth_files = [f for f in os.listdir(ground_truth_folder) if f.endswith(".png") or f.endswith(".jpg")]

    for gt_file in ground_truth_files:
        ground_truth_path = os.path.join(ground_truth_folder, gt_file)
        predicted_path = os.path.join(predicted_folder, gt_file)

        ground_truth = Image.open(ground_truth_path)
        predicted = Image.open(predicted_path)

        psnr_score, ssim_score, lpips_score = calculate_metrics(ground_truth, predicted)
        print(f"Image: {gt_file}")
        print(f"  PSNR: {psnr_score:.2f}")
        print(f"  SSIM: {ssim_score:.2f}")
        print(f"  LPIPS: {lpips_score:.4f}")

if __name__ == "__main__":
    scenes = [0, 1, 2, 3, 4]
    for scene in scenes:
        evaluate_scene(scene)
