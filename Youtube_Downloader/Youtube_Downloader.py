# Python3 !
# Youtube_Downloader.py ! -- A simple python program to download Youtube Videos

# Download the library by using the following command using terminal/cmd
# pip install pytube

# importing the module
from pytube import YouTube

link = input("Enter your Youtube Video URL: ")

try:
    # object creation using YouTube
    # which was imported in the beginning
    yt = YouTube(link)
    print("Connection Build Successfully.\n")
except:
    print("Connection Error")  # to handle exception

# This will stream all the available format for video
videos = yt.streams

# This will be index all the format in list starting with zero
video = list(enumerate(videos))
for i in video:
    # This will print all the available format of videos
    print(i)

# Ask user which format he wanted to download
download_option = int(input("\nEnter the desired Option to Download the Video: "))
download_video = videos[download_option]
download_video.download()  # for downloading the video

print("\nDownloaded Successfully !!!!!!!")
