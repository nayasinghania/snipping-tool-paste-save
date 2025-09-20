# Snipping Tool Save Dialog On Paste
A small python utility that, upon pasting an image, asks where you want to save the file and with what filename, then replaces the default `image.png` pasted.

## Setup
1. `pip install -r requirements.txt`

## Running
1. `python main.py`
2. Stop with `ctrl-c`

## Packaging
This code can be packaged as `snipping-tool-save-utility.exe`
1. `sh package.sh`
2. Run `snipping-tool-save-utility.exe` in `dist/`
3. Currently the only way to stop the exe is to end the `snipping-tool-save-utility.exe` task in your task manager
