
"""
Created on Tue Jul 14 12:38:31 2020

@author: Sivaraman Sivaraj
"""

import moviepy.editor

#Replace the parameter with the location of video

video = moviepy.editor.VideoFileClip("sample.mp4")
audio = video.audio

#replace the parameter with the location along with filename

audio.write_audiofile("result.mp3")
