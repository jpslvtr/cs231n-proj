import os
import subprocess

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:
            print(output.strip().decode())
    rc = process.poll()
    return rc

def ensure_directory_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def process_scene(scene_num):
    base_path = f"data/processed/scene{scene_num}"
    database_path = os.path.join(base_path, 'distorted/database.db')
    sparse_path = os.path.join(base_path, 'distorted/sparse')
    undistorted_path = os.path.join(base_path, 'undistorted')
    input_path = base_path

    ensure_directory_exists(os.path.dirname(database_path))
    ensure_directory_exists(sparse_path)
    ensure_directory_exists(undistorted_path)

    feature_extractor_cmd = f"colmap feature_extractor --database_path '{database_path}' --image_path '{input_path}' --ImageReader.single_camera 1"
    run_command(feature_extractor_cmd)
    
    feature_matching_cmd = f"colmap exhaustive_matcher --database_path '{database_path}' --SiftMatching.use_gpu 1"
    run_command(feature_matching_cmd)

    mapper_cmd = f"colmap mapper --database_path '{database_path}' --image_path '{input_path}' --output_path '{sparse_path}'"
    run_command(mapper_cmd)

    run_command(f"colmap patch_match_stereo --workspace_path {base_path} --workspace_format COLMAP --PatchMatchStereo.max_image_size 2000 --PatchMatchStereo.geom_consistency true")
    run_command(f"colmap stereo_fusion --workspace_path {base_path} --workspace_format COLMAP --input_type geometric --output_path {base_path}/fused.ply")
    run_command(f"colmap poisson_mesher --input_path {base_path}/fused.ply --output_path {base_path}/meshed-poisson.ply")
    run_command(f"colmap delaunay_mesher --input_path {base_path}/fused.ply --input_type dense --output_path {os.path.join(base_path, 'meshed-delaunay.ply')}")

    if os.path.exists(undistorted_images_path):
        shutil.rmtree(undistorted_images_path)
    shutil.copytree(input_path, undistorted_images_path)

    if os.path.exists(os.path.join(undistorted_path, 'sparse')):
        shutil.rmtree(os.path.join(undistorted_path, 'sparse'))
    shutil.copytree(sparse_path, os.path.join(undistorted_path, 'sparse'))

if __name__ == "__main__":
    scenes = [0, 1, 2, 3, 4]
    for scene in scenes:
        process_scene(scene)
