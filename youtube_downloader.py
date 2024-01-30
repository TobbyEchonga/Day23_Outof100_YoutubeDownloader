from pytube import YouTube

def download_video(video_url, output_path='.'):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Download the video
        print(f"Downloading: {yt.title}")
        video_stream.download(output_path)
        print("Download complete!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example: Replace 'VIDEO_URL' with the YouTube video URL
    video_url = 'VIDEO_URL'
    download_video(video_url)
