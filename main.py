import os
from pytube import YouTube, Stream
from spleeter.separator import Separator
from spleeter.audio import Codec

# Directories for input and output
script_dir = os.path.dirname(os.path.abspath(__file__))
raw_songs_path = os.path.join(script_dir, "raw")
converted_output_path = os.path.join(script_dir, "separated")


def download_youtube_mp3(url: str) -> str:
    """
    Downloads the MP3 audio from a YouTube video.

    Args:
        url (str): URL of the YouTube video.

    Returns:
        str: Full path to the downloaded file.
    """
    try:
        yt = YouTube(url)
        print(f'Getting streams for "{yt.title}"...')
        # Get the best available audio stream
        first: Stream = yt.streams.filter(only_audio=True).desc()[0]
        print(f'Started downloading "{yt.title}"...')
        result = first.download(output_path=raw_songs_path)
        print(f'Finished download of "{yt.title}".')
        return result
    except Exception as e:
        print(f'Error trying to download YouTube song "{url}". The error: {e}')


def generate_backingtracks_4stems():
    """
    Separates the downloaded raw audio files into 4 stems using Spleeter.
    """
    print(f'Starting to separate raw downloaded files...')
    separator = Separator('spleeter:4stems')
    for item in os.listdir(raw_songs_path):
        full_path = os.path.join(raw_songs_path, item)
        if os.path.isfile(full_path):
            print(f'Starting to separate "{item}"...')
            try:
                separator.separate_to_file(
                    audio_descriptor=full_path,
                    destination=converted_output_path,
                    codec=Codec.MP3
                )
                print(f'Finished separation of "{item}".')
            except Exception as e:
                print(f'Error on separating "{item}". The error: {e}')


if __name__ == '__main__':
    try:
        with open('inputs.txt', 'r', encoding="utf-8") as file:
            for url in file:
                download_youtube_mp3(url.strip())
        generate_backingtracks_4stems()
        print(f"Finished all conversions of the videos from 'inputs.txt'.")
    except Exception as e:
        print(f"Error: {e}")
