from moviepy.editor import VideoFileClip, AudioFileClip

# Ajuste de video estar vindo sem audio
def fix_audio(path_v, path_a, output_v_path_file):

    video = VideoFileClip(path_v)
    audio = AudioFileClip(path_a)

    video = video.set_audio(audio)

    video.write_videofile(f'{output_v_path_file}.mp4', codec='libx264', audio_codec='aac')

    video.close()
    audio.close()