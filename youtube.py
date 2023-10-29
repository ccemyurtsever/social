from pytube import YouTube

def fastYoutube(link):
    YouTube(f"{link}").streams.first().download()

def ytMp3Download(url):
    YouTube(url).streams.filter(res="mp3").first().download()

# def ytDownload(url,quality,fps):
#     if quality == "1080p":
#         if fps == 60:
#             YouTube(url).streams.filter(res=quality).filter(fps=fps).first().download()


def ytDownload(url,quality,fps):
    with YouTube(url).streams.filter(res=quality).filter(fps=fps).first().download() as download:
        if quality == "144p":
            if fps == 30:
                download
            else:
                print("Youtube")
        elif quality == "240p":
            if fps == 30:
               download
            else:
                print("Youtube")
        elif quality == "360p":
            if fps == 30:
                download
            else:
                print("Youtube")
        elif quality == "480p":
            if fps == 30:
                download
            else:
                print("Youtube")
        elif quality == "720p":
            if fps == 30:
                download
            elif fps == 60:
                download
        elif quality == "1080p":
            if fps == 30:
                download
            elif fps == 60:
                download
        elif quality == "1440p":
            if fps == 30:
                download
            elif fps == 60:
                download
        elif quality == "2160p":
            if fps == 30:
                download
            elif fps == 60:
                download
        elif quality == "4320p":
            if fps == 30:
                download
            elif fps == 60:
                download
        else:
            return


