import pytube
url = input ("url giriniz")
from pytube import YouTube
path = ""
pytube.YouTube(url).streams.get_highest_resolution().download(path)
