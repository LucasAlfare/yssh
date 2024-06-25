# yssh 👌

_Note:_ _"yssh"_ stands for "Youtube Songs Separation Helper"

This project helps me to automatically download songs from YouTube and generate their respective separate instruments tracks. This is done by using the library [pytube](https://github.com/pytube/pytube) to download the audio files and [Spleeter](https://github.com/deezer/spleeter) to automatically separate instrument tracks from the downloaded files.

# Usage 🛠
You can run `pip install -r requirements.txt` to setup dependencies (check [requirements file](requirements.txt) to see the dependencies).

After that, you need to add all the desired youtube URLs in a file called `inputs.txt` (same directory of the script). One URL by line, like following:

Contents for `inputs.txt`:
```plain-text
https://www.youtube.com/watch?v=kMxThvH-6Tw
https://www.youtube.com/watch?v=7ObT7LQd6ls
```

Thats said, you can run `python main.py`, wait the process and enjoy the conversions. in the directory `/separated`. 😃

⚠ _Quick note: the process is finished when console prompts the messa "`Finished all conversions of the videos from 'inputs.txt'.`"_
