# Snipping Tool Save Dialog On Paste
A small python utility that, upon pasting an image, asks where you want to save the file and with what filename, then replaces the default `image.png` pasted.

## Setup
1. `pip install -r requirements.txt`

## Running
1. `python main.py`
2. Stop with `ctrl-c`

## Packaging
This code can be packaged as `snip-util.exe`
1. `sh package.sh`
2. Find `snip-util.exe` in `dist/`