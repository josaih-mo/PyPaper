import os
import time
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from ctypes import windll

def browse_folder():
    folder_path = filedialog.askdirectory()
    textbox.delete(0, tk.END)
    textbox.insert(0, folder_path)

def change_wallpaper():
    folder_path = textbox.get()
    if not os.path.isdir(folder_path):
        messagebox.showerror("Error", "Invalid folder path")
        return
    
    images = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png")]
    if not images:
        messagebox.showerror("Error", "No images found in the folder")
        return
    
    messagebox.showwarning("Warning", "The only way to stop the wallpaper changing is to stop the Python process entirely. Are you sure you want to do this?")
    
    fps = float(fps_textbox.get())
    while True:
        for image in images:
            windll.user32.SystemParametersInfoW(20, 0, image, 0)
            time.sleep(1/fps)

root = tk.Tk()
root.title("PyPaper - Wallpaper Engine without the cost")

textbox = tk.Entry(root)
textbox.insert(0, os.path.dirname(__file__) + "\\exampleWallpaper")
textbox.pack()

browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.pack()

fps_label = tk.Label(root, text="FPS:")
fps_label.pack()

fps_textbox = tk.Entry(root)
fps_textbox.insert(0, "30")
fps_textbox.pack()

run_button = tk.Button(root, text="Run", command=change_wallpaper)
run_button.pack()

root.mainloop()
