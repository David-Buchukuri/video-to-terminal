<h1>getting started</h1>

1\. clone repo

```sh
git clone https://github.com/David-Buchukuri/video-to-terminal
```

<br>

2\. go to the root of the project and install dependencies

```sh
pip install -r requirments.txt
```

<br>

3\. to generate frames from the video run `generateFrames.py` file

4\. to render generated frames in the terminal run `index.py` file. Don't forget to zoom out your terminal a bit.

5\. to generate frames from your own videos, add desired video in `videos` folder, and in `generateFrames.py` replace function argument on line number 38 with the path of your file, if video contains any colors other than black and white you need to pass `True` as a second argument.
then go through step number 3 and 4 again.

recommended format for videos are mp4, other formats might work as well, but this script is tested using only mp4 files.

<br>
<br>
<br>
<br>
<br>

---

if you don't want to install dependencies globally, you can create virtual environment.

<br>

1\. once you clone the repo, cd into it and run

```sh
python3 -m venv terminal-to-video-venv
```

<br>

2\. to activate newly created virtual environment run

```sh
source terminal-to-video-venv/bin/activate
```

<br>

3\. now you can install dependencies

```sh
pip install -r requirments.txt
```

<br>
<br>

once you are done tinkering with project you can deactivate venv by running

```sh
deactivate
```
