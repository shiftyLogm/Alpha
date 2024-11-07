from os import chdir
from subprocess import run

def merge_ffmpeg(v_p: str, a_p: str, path: str, final_t: str) -> None:

    # This code is necessary because of the DASH format used on YouTube. 
    # Videos above 360p have their audio and video streams separated for better performance.
    # Do not delete or move this folder to another location.
    
    chdir(r"ffmpeg/bin")

    # Run the ffmpeg command to merge audio in video
    run([
        'ffmpeg', 
        '-i',
        v_p,
        '-i',
        a_p,
        '-c',
        'copy',
        f'{path}/{final_t}.mp4'],
        )