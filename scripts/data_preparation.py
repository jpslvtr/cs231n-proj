import os

# Define your video file and output directory
video_file = "data/raw/kilo.mp4"
output_dir = "data/processed"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Define the scenes with start and end times
scenes = [
    {"start": "00:00:00", "end": "00:00:05", "scene": "scene1"},
    {"start": "00:00:06", "end": "00:00:09", "scene": "scene2"},
    {"start": "00:00:10", "end": "00:00:16", "scene": "scene3"},
    {"start": "00:00:17", "end": "00:00:18", "scene": "scene4"},
]

# Extract frames for each scene
for scene in scenes:
    scene_output_dir = os.path.join(output_dir, scene["scene"])
    os.makedirs(scene_output_dir, exist_ok=True)
    ffmpeg_command = f"ffmpeg -i {video_file} -ss {scene['start']} -to {scene['end']} -vf 'fps=30' {scene_output_dir}/frame_%04d.png"
    os.system(ffmpeg_command)
