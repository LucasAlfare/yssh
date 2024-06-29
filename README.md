# yssh 👌

_Note:_ _"yssh"_ stands for "Youtube Songs Separation Helper".

This project helps to automatically download songs from YouTube and generate their respective separate instrument tracks. This is achieved using the library [pytube](https://github.com/pytube/pytube) to download the audio files and [Spleeter](https://github.com/deezer/spleeter) to automatically separate instrument tracks from the downloaded files.

## Usage 🛠
1. **Install Python**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/). Follow the installation instructions for your operating system. During installation, make sure to check the box to add Python to your PATH.

2. **Set up dependencies**: Run `pip install -r requirements.txt` to install all the necessary dependencies. Check the [requirements file](requirements.txt) to see the dependencies.

3. **Prepare input URLs**: Add all the desired YouTube URLs in a file called `inputs.txt` (in the same directory as the script). Enter one URL per line, as shown below:
  Example contents for `inputs.txt`:
  ```plain-text
  https://www.youtube.com/watch?v=kMxThvH-6Tw
  https://www.youtube.com/watch?v=7ObT7LQd6ls
  ```

4. **Run the script**: Run `python main.py`, wait for the process to complete, and enjoy the conversions. They will be placed in the `/separated` directory.

  ⚠ _Quick note: the process is finished when console displays the message "`Finished all conversions of the videos from 'inputs.txt'.`"_
