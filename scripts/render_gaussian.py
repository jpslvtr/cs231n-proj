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

def render_gaussian(scene_num, iteration=30000):
    project_path = '/content/drive/My Drive/cs231n/project/'
    output_base_path = project_path + 'output/'

    scene_folder = f'scene{scene_num}'
    output_model_dir = os.path.join(output_base_path, scene_folder, 'model')
    output_video_path = os.path.join(output_base_path, f'scene{scene_num}_video.mp4')
    images_dir = os.path.join(output_model_dir, 'images')

    render_script_path = '/content/gaussian-splatting/render.py'
    render_cmd = f"python {render_script_path} --model_path '{output_model_dir}' --iteration {iteration}"
    run_command(render_cmd)

    ffmpeg_cmd = f"ffmpeg -y -framerate 3 -i '{images_dir}/%05d.png' -vf 'pad=ceil(iw/2)*2:ceil(ih/2)*2' '{output_video_path}'"
    run_command(ffmpeg_cmd)

if __name__ == "__main__":
    scenes = [0, 1, 2, 3, 4]
    for scene in scenes:
        render_gaussian(scene)
