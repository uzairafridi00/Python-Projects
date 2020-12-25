# python3!
# instaprofileDownloader.py - This code snippet download profile picture by providing a username
# You will find profile picture on Desktop


import os
import instaloader


def downloader(username):
    instance = instaloader.Instaloader()
    # Change working directory to Desktop
    os.chdir(os.path.join(os.path.expanduser("~"), "Desktop"))
    return instance.download_profile(username, profile_pic_only=True)


if __name__ == "__main__":
    print("Enter username: ")
    username = input(r" >>")
    downloader(username)
