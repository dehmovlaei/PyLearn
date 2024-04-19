from threading import Thread
from moviepy import editor
import time


def convert(add, name):
    video = editor.VideoFileClip(add)
    video.audio.write_audiofile(f'{name}.mp3')


videos = [["./01.mp4", "01"],
          ["./02.mp4", "02"],
          ["./03.mp4", "03"],
          ["./04.mp4", "04"],
          ["./05.mp4", "05"]]

start_time = time.time()
threads = []

for add, name in videos:
    threads.append(Thread(target=convert, args=(add, name)))

for thread in threads:
    thread.start()
    thread.join()

end_time = time.time()
print(f'{end_time - start_time}_on thread mod')

start_time = time.time()

for add, name in videos:
    convert(add, name)

end_time = time.time()
print(f'{end_time - start_time}_on simple mod')