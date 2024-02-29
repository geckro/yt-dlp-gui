import yt_dlp


def download_video(url: str):
    with yt_dlp.YoutubeDL() as ytdlp:
        ytdlp.download(url)
