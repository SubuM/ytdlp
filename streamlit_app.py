

import streamlit as st
import yt_dlp
import subprocess
from io import BytesIO
import os
import time


def housekeeping(file):
    os.remove(f'./{file}')
    time.sleep(5)
    st.write('File successfully downloaded!')


def down_vid(yt):
    local_file = 'downloaded_file'
    # Create a dictionary for the download options
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Download the best video and audio
        'outtmpl': f'./{local_file}.%(ext)s',  # Set output file name and location
        'merge_output_format': 'mp4',  # Merge video and audio into an MP4 format
        'postprocessors': [{  # Post-process to merge video and audio if necessary
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Convert to MP4
        }],
        'noplaylist': True,  # Avoid downloading playlists
    }

    try:
        # Create a yt-dlp instance and download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt])

        filename = subprocess.getoutput(f'yt-dlp --print filename {yt}').rsplit(
            '.'+subprocess.getoutput(f'yt-dlp --print filename -o "%(ext)s" {yt}'))[0]
        local_file += '.mp4'

        with open(f'./{local_file}', 'rb') as fh:
            buf = BytesIO(fh.read())
        fh.close()

        if st.download_button('Download Video', data=buf, file_name=filename, mime='video/mp4'):
            housekeeping(local_file)

    except Exception as down_err:
        st.write(f'Error is: {down_err}')


def down_aud(yt):
    local_file = 'downloaded_file'
    # Create a dictionary for the download options
    ydl_opts = {
        'format': 'bestaudio/best',  # Download the best audio
        'outtmpl': f'./{local_file}.%(ext)s',  # Set output file name and location
        'merge_output_format': 'mp3',  # Merge video and audio into an MP3 format
        'postprocessors': [{  # Post-process to merge video and audio if necessary
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp3',  # Convert to MP3
        }],
        'noplaylist': True,  # Avoid downloading playlists
    }

    try:
        # Create a yt-dlp instance and download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt])

        filename = subprocess.getoutput(f'yt-dlp --print filename {yt}').rsplit(
            '.' + subprocess.getoutput(f'yt-dlp --print filename -o "%(ext)s" {yt}'))[0]
        local_file += '.mp3'

        with open(f'./{local_file}', 'rb') as fh:
            buf = BytesIO(fh.read())
        fh.close()

        if st.download_button('Download Audio', data=buf, file_name=filename, mime='audio/mp3'):
            housekeeping(local_file)

    except Exception as down_err:
        st.write(f'Error is: {down_err}')


def set_config():
    # setting page icon
    st.set_page_config(page_title='Download YouTube Video/Audio',
                       page_icon='timer_clock', initial_sidebar_state='auto')

    # hide hamburger menu and footer logo
    hide_st_style = """
                        <style>
                        #MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}
                        </style>
                        """
    st.markdown(hide_st_style, unsafe_allow_html=True)


def get_link():
    dlink = st.text_input('Enter YouTube link here:', help='Enter YouTube link to be downloaded',
                          placeholder='Enter YouTube link here')
    if dlink:
        st.write('Choose Video or Audio to download:')

        option = st.radio('Choose Video or Audio to download:', options=('Video', 'Audio'), index=None)

        if option == 'Video':
            down_vid(dlink)
        elif option == 'Audio':
            down_aud(dlink)


def download_app():
    set_config()
    get_link()


if __name__ == '__main__':
    download_app()
