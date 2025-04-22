# youtube_downloader.py

from pytube import YouTube

def download_video():
    url = input("Enter the YouTube video URL: ").strip()
    try:
        yt = YouTube(url)
        print(f"Title: {yt.title}")
        print("Downloading...")
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print("Download completed!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    download_video()
