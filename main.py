import tkinter as tk
from tkinter import filedialog

def main():
    root = tk.Tk()
    root.withdraw()
    try:
        while True:
            print("Hello, World!")
            file_path = filedialog.askopenfilename(
                title="Select a file",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            if file_path:
                print("You selected:", file_path)
            else:
                print("No file selected.")
    except KeyboardInterrupt:
        print("\n🛑 Exiting...")

if __name__ == "__main__":
    main()
