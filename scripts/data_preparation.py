import os

video_file = "data/raw/submarine_video.mp4"
output_dir = "data/processed"

os.makedirs(output_dir, exist_ok=True)

scenes = [
    {"start": "00:00:00", "end": "00:00:05", "scene": "scene1"},
    {"start": "00:00:06", "end": "00:00:09", "scene": "scene2"},
    {"start": "00:00:10", "end": "00:00:16", "scene": "scene3"},
    {"start": "00:00:17", "end": "00:00:18", "scene": "scene4"},
]

for scene in scenes:
    scene_output_dir = os.path.join(output_dir, scene["scene"])
    os.makedirs(scene_output_dir, exist_ok=True)
    
    ffmpeg_command = f"ffmpeg -i {video_file} -ss {scene['start']} -to {scene['end']} -vf 'fps=30' {scene_output_dir}/frame_%04d.png"
    os.system(ffmpeg_command)
    
    for frame_file in os.listdir(scene_output_dir):
        frame_path = os.path.join(scene_output_dir, frame_file)
        normalize_command = f"convert {frame_path} -resize 1080x720! {frame_path}"
        os.system(normalize_command)
        
        # Apply random cropping, rotation, and color adjustments maybe