import ctypes
import os
import json
import time
plsCont = False
print("PyPaper 1.0.0")
try:
    with open("pyPaper.json") as settingsRaw:
        settings = json.load(settingsRaw)
        paths1 = os.path.dirname(__file__) or '.'
        path = paths1 + "\\" + settings['RelativePyPaperPath']
        frames = 0
        try:
            for i,file in enumerate(os.listdir(path)):
                if file.endswith(".png"):
                    frames += 1
            if frames > 1:
                print("PyPaper has frames!")
                plsCont = True
            else:
                print("No frames in PyPaper!")
            
        except FileNotFoundError:
            print("No PyPaper found!")
except FileNotFoundError:
    print("PyPaper has no settings JSON!")
    settingsRaw = {
        "RelativePyPaperPath": input("What is the RELATIVE path to your PyPaper, not including \".\\\"? >").replace("\\", "\\\\")
    }
    settings = json.dumps(settingsRaw, indent=4)
    with open("pyPaper.json", "w") as pyPaper:
        pyPaper.write(settings)
        print("Please run PyPaper again!")

if (plsCont):
    frames = 0
    fps = float(input("What is your desired FPS? >"))
    frameNames = input("What is the name of your frames (not including the number of frames, e.g. if you passed Frame, we'd use Frame1, Frame2, and etc.)")
    while True:
        for i,file in enumerate(os.listdir(path)):
                if file.endswith(".png"):
                    frames += 1
                    ctypes.windll.user32.SystemParametersInfoW(20, 0, path + "\\" + frameNames  + str(frames) + ".png", 0)
                    print(path + frameNames + str(frames))
                    time.sleep(fps)
        frames = 0
