import tkinter as tk
from tkinter import filedialog
import os

def get_filename():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    filename = filedialog.askopenfilename(
        title="Select a Text File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    basename = os.path.basename(filename)
    print("Selected file:", basename)
    return basename

if __name__ == "__main__":
    get_filename()
