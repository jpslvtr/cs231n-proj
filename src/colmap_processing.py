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
    database_path = os.path.join(base_path, 'database.db')
    sparse_path = os.path.join(base_path, 'sparse')
    
    ensure_directory_exists(os.path.dirname(database_path))
    ensure_directory_exists(sparse_path)
    
    feature_extractor_cmd = f"colmap feature_extractor --database_path {database_path} --image_path {base_path}"
    run_command(feature_extractor_cmd)
    
    feature_matching_cmd = f"colmap exhaustive_matcher --database_path {database_path}"
    run_command(feature_matching_cmd)
    
    mapper_cmd = f"colmap mapper --database_path {database_path} --image_path {base_path} --output_path {sparse_path}"
    run_command(mapper_cmd)
    
    pmvs_cmd = f"colmap image_undistorter --image_path {base_path} --input_path {sparse_path} --output_path {base_path}/dense"
    run_command(pmvs_cmd)
    
    poisson_cmd = f"colmap poisson_mesher --input_path {base_path}/dense/fused.ply --output_path {base_path}/meshed-poisson.ply"
    run_command(poisson_cmd)

if __name__ == "__main__":
    scenes = [1, 2, 3, 4]
    for scene in scenes:
        process_scene(scene)