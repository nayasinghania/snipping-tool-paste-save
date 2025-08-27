#!/bin/bash
# Build the snipping tool utility as a single executable with icon

pyinstaller --onefile --windowed --icon=icon.ico --name=snip-util main.py