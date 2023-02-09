import sys
import os
import ctypes
import time

def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

if __name__ == '__main__':
    folder = sys.argv[1]
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            set_wallpaper(file_path)
            time.sleep(1 / 30)
