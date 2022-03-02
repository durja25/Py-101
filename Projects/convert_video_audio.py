# Python code to convert video to audio
import moviepy.editor as mp

# Insert Local Video File Path
clip = mp.VideoFileClip(r"input_video")

# subclip(start,endtime)

# Insert Local Audio File Path
clip.audio.write_audiofile(r"out.mp3")