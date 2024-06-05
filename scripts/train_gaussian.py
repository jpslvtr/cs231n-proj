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

def train_gaussian(scene_num):
    project_path = '/content/drive/My Drive/cs231n/project/'
    frames_path = project_path + 'framesv4/'
    output_base_path = project_path + 'output/'

    scene_folder = f'scene{scene_num}'
    unzip_dir = os.path.join(output_base_path, scene_folder, 'images')
    output_model_dir = os.path.join(output_base_path, scene_folder, 'model')

    os.makedirs(output_model_dir, exist_ok=True)

    train_script_path = '/content/gaussian-splatting/train.py'
    train_cmd = f"python {train_script_path} -s '{unzip_dir}' -o '{output_model_dir}'"
    run_command(train_cmd)

if __name__ == "__main__":
    scenes = [0, 1, 2, 3, 4]
    for scene in scenes:
        train_gaussian(scene)
