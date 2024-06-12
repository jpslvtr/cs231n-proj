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

def train_gaussian(scene_num, iterations):
    project_path = 'data/'
    frames_path = os.path.join(project_path, 'processed', f'scene{scene_num}')
    output_base_path = os.path.join(project_path, 'output', f'scene{scene_num}')
    
    unzip_dir = os.path.join(output_base_path, 'images')
    output_model_dir = os.path.join(output_base_path, 'model')
    
    os.makedirs(output_model_dir, exist_ok=True)
    
    train_script_path = 'src/train_gaussian.py'
    train_cmd = f"python {train_script_path} --frames_path {frames_path} --output_path {output_model_dir} --iterations {iterations}"
    run_command(train_cmd)

if __name__ == "__main__":
    train_gaussian(1, iterations=15000)
    train_gaussian(2, iterations=7000)