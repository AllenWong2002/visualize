from moviepy import *

# Load the two videos
video1 = VideoFileClip("b.mp4")
video2 = VideoFileClip("output_H264.mp4")

# Resize videos to have the same height (optional)
video1_resized = video1.resized(height=video2.h)

# Ensure both videos have the same duration (optional, if durations are different)
min_duration = min(video1.duration, video2.duration)
video1_resized = video1_resized.subclipped(0, min_duration)
video2 = video2.subclipped(0, min_duration)

# Merge videos side-by-side
final_video = clips_array([[video1_resized, video2]])

# Write the result to a file with H.264 encoding
final_video.write_videofile(
    "output.mp4",
    codec="libx264",  # H.264 codec
    audio_codec="aac",  # AAC audio codec
    preset="medium",  # Adjust preset for speed vs. quality balance
    bitrate="5000k"  # Optional: Specify a bitrate for quality control
)
