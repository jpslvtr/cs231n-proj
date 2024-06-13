import data_preparation
import colmap_processing
import train_gaussian
import render_gaussian
import evaluate_metrics

def main():
    data_preparation.prepare_dataset()
    
    scenes = [1, 2, 3, 4]
    for scene in scenes:
        colmap_processing.process_scene(scene)
    
    train_gaussian.train_gaussian(1, iterations=15000)
    train_gaussian.train_gaussian(2, iterations=7000)
    
    for scene in scenes:
        render_gaussian.render_gaussian(scene)
    
    evaluate_metrics.evaluate_scenes(scenes)

if __name__ == "__main__":
    main()