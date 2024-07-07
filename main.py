from pytube import Playlist, YouTube
import os
from pydub import AudioSegment


def download_youtube_playlist_as_mp3(playlist_url, download_path):
    # Create a Playlist object
    playlist = Playlist(playlist_url)

    # Print the playlist title
    print(f'Downloading videos from playlist: {playlist.title}')

    # Create the download directory if it does not exist
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Iterate over each video in the playlist
    for video_url in playlist.video_urls:
        try:
            # Create a YouTube object for each video
            video = YouTube(video_url)
            print(f'Downloading: {video.title}')

            # Download the video
            video_stream = video.streams.filter(only_audio=True).first()
            downloaded_file_path = video_stream.download(download_path)

            # Convert the downloaded file to mp3
            audio = AudioSegment.from_file(downloaded_file_path)
            mp3_file_path = os.path.join(download_path, video.title + '.mp3')
            audio.export(mp3_file_path, format='mp3')

            # Remove the original downloaded file
            os.remove(downloaded_file_path)

            print(f'Successfully downloaded and converted: {video.title}')

        except Exception as e:
            print(f'Failed to download {video_url}. Reason: {e}')

    print('All videos have been downloaded and converted to MP3.')


# Example usage
playlist_url = ''
download_path = ''

download_youtube_playlist_as_mp3(playlist_url, download_path)
