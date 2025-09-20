#v1.0.0

from PIL import Image, ImageGrab
import tkinter as tk
from tkinter import filedialog
import keyboard
import os


def main():
    keyboard.wait("ctrl+v")
    print("Paste operation")
    im = ImageGrab.grabclipboard()
    if not isinstance(im, Image.Image):
        print("Clipboard does not contain an image. Skipping...")
        return
    file_path = filedialog.asksaveasfilename(
        title="Save image as...",
        defaultextension=".png",
        filetypes=[
            ("PNG files", "*.png"),
            ("JPEG files", "*.jpg;*.jpeg"),
            ("All files", "*.*"),
        ],
    )
    if file_path:
        im.save(file_path)
        print(f"Image saved to: {file_path}")
        directory = os.path.dirname(file_path)
        os.remove(os.path.join(directory, "image.png"))
        print(f"Deleted image.png from: {directory}")

    else:
        print("No file selected.")


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Stopping...")
        exit(0)
