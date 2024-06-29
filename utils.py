import os
from pytube import YouTube, Stream
from spleeter.separator import Separator
from spleeter.audio import Codec


class DownloadedSongInfo:
    """
    Represents information about a downloaded song.
    
    Attributes:
        original_url (str): The original URL of the song.
        output_os_path (str): The file path where the song was downloaded.
    """
    def __init__(self, original_url: str, output_os_path: str) -> None:
        """
        Initializes the DownloadedSongInfo object.
        
        Args:
            original_url (str): The original URL of the song.
            output_os_path (str): The file path where the song was downloaded.
        """
        self.original_url = original_url
        self.output_os_path = output_os_path
  
    def __str__(self) -> str:
        """
        Returns a string representation of the DownloadedSongInfo object.
        
        Returns:
            str: A string describing the DownloadedSongInfo object.
        """
        return f'DownloadedSongInfo(original_url="{self.original_url}", output_os_path="{self.output_os_path}")'
  

class SeparationInfo:
    """
    Represents information about the separation process.
    
    Attributes:
        input_path (str): The input file path.
        output_path (str): The output directory path.
        codec (Codec): The audio codec used for the output files.
    """
    def __init__(self, input_path: str, output_path: str, codec: Codec) -> None:
        """
        Initializes the SeparationInfo object.
        
        Args:
            input_path (str): The input file path.
            output_path (str): The output directory path.
            codec (Codec): The audio codec used for the output files.
        """
        self.input_path = input_path
        self.output_path = output_path
        self.codec = codec
  
    def __str__(self) -> str:
        """
        Returns a string representation of the SeparationInfo object.
        
        Returns:
            str: A string describing the SeparationInfo object.
        """
        return f'SeparationInfo(input_path="{self.input_path}", output_path="{self.output_path}", codec={self.codec})'


def download_youtube_audio(url: str, output_path: str) -> DownloadedSongInfo:
    """
    Downloads the audio from a YouTube video.

    Args:
        url (str): The URL of the YouTube video.
        output_path (str): The directory path where the audio will be saved.

    Returns:
        DownloadedSongInfo: Information about the downloaded song if successful, None otherwise.
    """
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            
        yt = YouTube(url)
        audio_stream: Stream = yt.streams.filter(only_audio=True).desc().first()
        output_file = audio_stream.download(output_path)
        
        return DownloadedSongInfo(original_url=url, output_os_path=output_file)
    except Exception as e:
        print(f'Error trying to download the URL {url}.')
        print(f'The error:\n{e}')
        return None
  

def separate_4stems(input_path: str, output_path: str, codec: Codec = Codec.MP3) -> SeparationInfo:
    """
    Separates the audio into 4 stems using Spleeter.

    Args:
        input_path (str): The input file path.
        output_path (str): The output directory path.
        codec (Codec): The audio codec used for the output files. Default is Codec.MP3.

    Returns:
        SeparationInfo: Information about the separation process if successful, None otherwise.
    """
    try:
        if not os.path.exists(input_path):
            print(f'Input path {input_path} does not exist.')
            return None
        
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            
        separator = Separator('spleeter:4stems')
        separator.separate_to_file(input_path, output_path, codec=codec)
        
        return SeparationInfo(input_path=input_path, output_path=output_path, codec=codec)
    except Exception as e:
        print(f'Error trying to separate stems for the input {input_path}.')
        print(f'The error:\n{e}')
        return None
