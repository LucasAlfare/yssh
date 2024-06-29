import utils
from spleeter.audio import Codec


def process_inputs_file(
  inputs_file_path: str,
  download_output: str,
  separations_output: str,
  separations_codec: Codec
):
  def process_single_url(url_str: str) -> dict:
    download_info = utils.download_youtube_audio(
      url=url_str,
      output_path=download_output
    )

    separation_info = utils.separate_4stems(
      input_path=download_info.output_os_path,
      output_path=separations_output,
      codec=separations_codec
    )

    return {'download_info': download_info, 'separation_info': separation_info}

  with open(inputs_file_path, 'r', encoding="utf-8") as file:
    for url_str in file:
      process_single_url(url_str)


if __name__ == '__main__':
  process_inputs_file(
    inputs_file_path='inputs.txt',
    download_output='my_test',
    separations_output='separated',
    separations_codec=Codec.MP3
  )
