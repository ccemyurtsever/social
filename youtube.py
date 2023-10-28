from pytube import YouTube

def fastYoutube(link):
    YouTube(f"{link}").streams.first().download()

def youtube(quality,link):
    if quality == "144p":
        pass
    elif quality == "240p":
        pass
    elif quality == "360p":
        pass
    elif quality == "480p":
        pass
    elif quality == "720p":
        pass
    elif quality == "1080p":
        pass
    elif quality == "1440p":
        pass
    elif quality == "2160p":
        pass
    else:
        print(f"Error\nYou selected a resolution ({quality}p) that is not available in the video.")    


def youtubeMp3(link):
    pass

