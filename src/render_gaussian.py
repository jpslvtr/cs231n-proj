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

def render_gaussian(scene_num):
    project_path = 'data/'
    output_base_path = os.path.join(project_path, 'output', f'scene{scene_num}')
    
    model_path = os.path.join(output_base_path, 'model')
    output_video_path = os.path.join(output_base_path, 'rendered_video.mp4')
    images_dir = os.path.join(model_path, 'images')
    
    render_script_path = 'src/render_gaussian.py'
    render_cmd = f"python {render_script_path} --model_path {model_path}"
    run_command(render_cmd)
    
    ffmpeg_cmd = f"ffmpeg -y -framerate 30 -i {images_dir}/%04d.png -c:v libx264 -pix_fmt yuv420p {output_video_path}"
    run_command(ffmpeg_cmd)

if __name__ == "__main__":
    scenes = [1, 2, 3, 4]
    for scene in scenes:
        render_gaussian(scene)