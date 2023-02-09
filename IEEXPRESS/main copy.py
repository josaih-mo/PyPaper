import ctypes
import os
import json
import time
plsCont = False
print("PyPaper 1.0.0")
try:
    with open(os.path.dirname(__file__) + "/pyPaper.json") as settingsRaw:
        settings = json.load(settingsRaw)
        paths1 = os.path.dirname(__file__) or '.'
        path = settings['PyPaperPath']
        frames = 0
        try:
            for i,file in enumerate(os.listdir(path)):
                if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                    frames += 1
            if frames > 1:
                print("PyPaper has frames!")
                plsCont = True
            else:
                print("No frames in PyPaper!")
            
        except FileNotFoundError:
            print("No PyPaper found!")
except FileNotFoundError:
    print("PyPaper has no settings JSON! " + os.path.dirname(__file__))
    settingsRaw = {
        "PyPaperPath": input("What is the EXACT path to your PyPaper? >").replace("\\", "\\\\")
    }
    settings = json.dumps(settingsRaw, indent=4)
    with open("pyPaper.json", "w") as pyPaper:
        pyPaper.write(settings)
        print("Please run PyPaper again!")

if (plsCont):
    fps = float(input("What is your desired FPS? >"))
    images = [os.path.join(path, file) for file in os.listdir(path) if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png")]
    while True:
        for image in images:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 0)
            time.sleep(1/fps)
