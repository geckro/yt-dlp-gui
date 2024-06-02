import yt_dlp

from log import log


def download_media(url: str, options: dict) -> None:
    """
    Downloads video or audio from the given url in yt-dlp.
    Args:
        url: a string of the url to download
        options: a dictionary containing CML flags for yt-dlp
    """
    try:
        if not url.strip():
            raise ValueError(f"Empty URL: {url}")
        with yt_dlp.YoutubeDL(options) as ytdlp:
            ytdlp.download(url)
    except yt_dlp.DownloadError as e:
        log("error", f"Cant download the URL: {e}")
