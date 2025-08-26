import keyboard
import time
from tkinter import filedialog, Tk
from PIL import ImageGrab, Image
import clipboard
from io import BytesIO

def paste_image(image: Image.Image):
    """Reinsert image into clipboard so Ctrl+V works."""
    output = BytesIO()
    image.convert("RGB").save(output, format="BMP")
    data = output.getvalue()
    clipboard.copy("")        # clear any text
    clipboard.copy_image(data) # put image into clipboard

def handle_paste():
    img = ImageGrab.grabclipboard()
    if img:
        root = Tk()
        root.withdraw()
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")],
            initialfile="screenshot.png"
        )
        if save_path:
            img.save(save_path, "PNG")
            print(f"Saved screenshot as {save_path}")
        root.destroy()

        paste_image(img)
        keyboard.send("ctrl+v")
    else:
        keyboard.send("ctrl+v")

keyboard.add_hotkey("ctrl+v", handle_paste, suppress=True)

print("Running... Press Ctrl+C to exit.")
while True:
    time.sleep(1)
