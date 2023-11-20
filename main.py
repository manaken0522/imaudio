import glob
from moviepy import editor

audios = glob.glob('./audios/*.mp3')
for audio in audios:
    audio = audio.replace('\\', '/')
    print(audio)
    img_clip = editor.ImageClip('./image.png')
    audio_clip = editor.AudioFileClip(audio)
    video_clip = img_clip.set_duration(audio_clip.duration)
    video_clip = video_clip.set_audio(audio_clip)
    video_clip.write_videofile(f'./output/{audio.replace("./audios/", "").replace(".mp3", "")}.mp4', fps=60)