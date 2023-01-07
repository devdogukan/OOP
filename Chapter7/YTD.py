from pytube import Playlist
import os
from tkinter import Tk
from tkinter import filedialog



url = input("Enter a url: ")
playlist = Playlist(url)
path = "C:\\Users\\dgnk6\\Desktop\\Music\\demo1"

choice = int(input("Enter your choice: 1.Video 2.MP3 :  "))

i = 1

if choice == 1:
	for video in playlist.videos:
		print(f'{i}. {video.title} downloding...')
		video.streams.get_highest_resolution().download(path)
		i += 1
  
elif choice == 2:
    for music in playlist.videos:
        print(f'{i}. {music.title} downloding...')
        out = music.streams.filter(only_audio=True).first().download(path)
        base, ext = os.path.splitext(out)
        newfile = base + ".mp3"
        os.rename(out, newfile)
        i += 1
    
print("Done")
    
    
"""
from pytube import YouTube, Playlist

pl_url = input("Enter YT Playlist URL: ")
pl = Playlist(pl_url)
print(f'\n Playlist Title: {pl.title}')

for yt_video_url in pl.video_urls:
	
	ytv = YouTube(yt_video_url)
	print(f'\n Video Title: {ytv.title}')
	print(f' Video URL: {yt_video_url}')

	ytv_streams = ytv.streams.all()
	ytv_streams_li = list((enumerate(ytv_streams)))

	print("\n Stream lists:")
	for stream in ytv_streams_li:
		print(stream)
	print()

	strm_no = int(input("Enter stream no: "))

	print(f' Downloading...:\n {ytv_streams[strm_no]}')
	ytv_streams[strm_no].download()
	print(f'\n Download Completed...:\n {ytv.title} \n {ytv_streams[strm_no]}')
"""