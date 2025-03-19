
import yt_dlp


def download_video(url, output_path='./'):
    # Create a dictionary for the download options
    ydl_opts = {
        'format': 'bestaudio/best',  # Download best audio
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Set output file name and location
        'merge_output_format': 'mp3',  # Merge audio into an MP3 format
        'postprocessors': [{  # Post-process to merge video and audio if necessary
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp3',  # Convert to MP3
        }],
        'noplaylist': True,  # Avoid downloading playlists
    }

    # Create a yt-dlp instance and download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


# Example usage
if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)

