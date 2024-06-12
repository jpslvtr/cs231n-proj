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
    base_path = f"data/output/scene{scene_num}"
    ground_truth_folder = os.path.join(base_path, "ground_truth")
    predicted_folder = os.path.join(base_path, "predicted")
    
    ground_truth_files = [f for f in os.listdir(ground_truth_folder) if f.endswith(".png") or f.endswith(".jpg")]
    
    psnr_scores = []
    ssim_scores = []
    lpips_scores = []
    
    for gt_file in ground_truth_files:
        ground_truth_path = os.path.join(ground_truth_folder, gt_file)
        predicted_path = os.path.join(predicted_folder, gt_file)
        
        ground_truth = Image.open(ground_truth_path)
        predicted = Image.open(predicted_path)
        
        psnr_score, ssim_score, lpips_score = calculate_metrics(ground_truth, predicted)
        psnr_scores.append(psnr_score)
        ssim_scores.append(ssim_score)
        lpips_scores.append(lpips_score)
    
    avg_psnr = np.mean(psnr_scores)
    avg_ssim = np.mean(ssim_scores)
    avg_lpips = np.mean(lpips_scores)
    
    print(f"Scene {scene_num} Evaluation:")
    print(f"  Average PSNR: {avg_psnr:.2f}")
    print(f"  Average SSIM: {avg_ssim:.2f}")
    print(f"  Average LPIPS: {avg_lpips:.4f}")
    
    return avg_psnr, avg_ssim, avg_lpips

if __name__ == "__main__":
    scenes = [1, 2, 3, 4]
    overall_psnr = []
    overall_ssim = []
    overall_lpips = []
    
    for scene in scenes:
        psnr, ssim, lpips = evaluate_scene(scene)
        overall_psnr.append(psnr)
        overall_ssim.append(ssim)
        overall_lpips.append(lpips)
    
    print("\nOverall Evaluation:")
    print(f"  Average PSNR: {np.mean(overall_psnr):.2f}")
    print(f"  Average SSIM: {np.mean(overall_ssim):.2f}")
    print(f"  Average LPIPS: {np.mean(overall_lpips):.4f}")