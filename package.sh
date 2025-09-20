#!/bin/bash
# Build the snipping tool utility as a single executable with icon

pyinstaller --onefile --windowed --icon=icon.ico --name=snipping-tool-save-utility main.py