import os

os.system("pip install SpeechRecognition moviepy")
os.system("pip install SpeechRecognition")
os.system("pip install moviepy")

from moviepy.editor import VideoFileClip
import os

def create_subtitles(video_file):
    clip = VideoFileClip(video_file)
    subtitles = clip.subclip(0, clip.duration).iter_frames()
    
    subtitle_text = ""
    current_time = 0
    
    for frame in subtitles:
        current_time += 1
        # Assuming frame is a frame object, you need to extract text from the frame
        # and add it to the subtitle_text with the current time
        subtitle_text += f"{current_time}s: {extract_text_from_frame(frame)}\n"
    
    return subtitle_text

def extract_text_from_frame(frame):
    # Extract text from the frame (you need to implement this based on your requirements)
    return "Subtitle text extracted from frame"

# Get a list of all video files in the current directory
video_files = [file for file in os.listdir() if file.endswith(('.mp4', '.avi', '.mkv', '.mov'))]

# Iterate over each video file
for video_file in video_files:
    print(f"\nVideo File: {video_file}")
    
    # Create subtitles for the video file
    subtitles = create_subtitles(video_file)
    
    # Save subtitles to a text file
    output_file = f"{os.path.splitext(video_file)[0]}.txt"
    with open(output_file, 'w') as file:
        file.write(subtitles)

# softy_plug