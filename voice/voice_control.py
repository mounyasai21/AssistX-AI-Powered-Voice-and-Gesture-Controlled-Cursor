import speech_recognition as sr
import subprocess
import sys
import os
import pyautogui

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.system_commands import *

# ---------------- VOICE SETTINGS ---------------- #

recognizer = sr.Recognizer()
recognizer.energy_threshold = 250
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.5

mic = sr.Microphone()

print("🎤 AssistX Voice Control Started")

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
gesture_script = os.path.join(base_dir, "gesture", "main.py")

gesture_process = None

# ---------------- OPEN FILE/FOLDER SEARCH ---------------- #

def search_and_open(name, search_type="folder"):

    search_locations = [
        os.path.join(os.path.expanduser("~"), "Desktop"),
        os.path.join(os.path.expanduser("~"), "Documents"),
        os.path.join(os.path.expanduser("~"), "Downloads"),
        os.path.expanduser("~")
    ]

    name = name.lower()

    for location in search_locations:

        for root, dirs, files in os.walk(location):

            if search_type == "folder":

                for d in dirs:

                    if name in d.lower():

                        path = os.path.join(root, d)

                        os.startfile(path)

                        print("📂 Opening folder:", path)

                        return

            if search_type == "file":

                for f in files:

                    if name in f.lower():

                        path = os.path.join(root, f)

                        os.startfile(path)

                        print("📄 Opening file:", path)

                        return

    print("❌ Not found")


while True:

    with mic as source:

        print("🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=0.3)

        audio = recognizer.listen(source, phrase_time_limit=4)

    try:

        command = recognizer.recognize_google(audio).lower()

        print("Command:", command)

        # -------- MODE -------- #

        if "gesture" in command:

            print("Starting Gesture Mode")

            if gesture_process is None:

                gesture_process = subprocess.Popen(
                    [sys.executable, gesture_script]
                )

        elif "stop gesture" in command:

            if gesture_process:

                gesture_process.terminate()

                gesture_process = None

                print("Gesture mode stopped")

        elif "stop voice" in command:

            print("Voice stopped")

            break

        # -------- CURSOR MOVEMENT -------- #

        elif "move cursor left" in command:
            pyautogui.moveRel(-200,0)

        elif "move cursor right" in command:
            pyautogui.moveRel(200,0)

        elif "move cursor up" in command:
            pyautogui.moveRel(0,-200)

        elif "move cursor down" in command:
            pyautogui.moveRel(0,200)

        # ---- SMALL MOVEMENT ---- #

        elif "move cursor little left" in command:
            pyautogui.moveRel(-50,0)

        elif "move cursor little right" in command:
            pyautogui.moveRel(50,0)

        elif "move cursor little up" in command:
            pyautogui.moveRel(0,-50)

        elif "move cursor little down" in command:
            pyautogui.moveRel(0,50)

        # -------- MOUSE -------- #

        elif "left click" in command:
            left_click()

        elif "right click" in command:
            right_click()

        elif "double click" in command:
            double_click()

        # -------- SCROLL -------- #

        elif "scroll up" in command:
            scroll_up()

        elif "scroll down" in command:
            scroll_down()

        # -------- COPY PASTE -------- #

        elif "copy" in command:
            pyautogui.hotkey("ctrl","c")
            print("Copied")

        elif "paste" in command:
            pyautogui.hotkey("ctrl","v")
            print("Pasted")

        # -------- SELECT ALL -------- #

        elif "select all" in command:
            select_all()

        # -------- TAB SWITCH -------- #

        elif "switch tab" in command or "tab switch" in command:
            pyautogui.hotkey("alt","tab")
            print("Tab switched")

        # -------- SCREENSHOT -------- #

        elif "screenshot" in command:
            take_screenshot()

        # -------- ZOOM -------- #

        elif "zoom in" in command:
            pyautogui.hotkey("ctrl","+")
            print("Zoom In")

        elif "zoom out" in command:
            pyautogui.hotkey("ctrl","-")
            print("Zoom Out")

        # -------- VOLUME -------- #

        elif "volume up" in command:
            volume_up()

        elif "volume down" in command:
            volume_down()

        # -------- BRIGHTNESS -------- #

        elif "brightness up" in command:
            brightness_up()

        elif "brightness down" in command:
            brightness_down()

        # -------- BROWSER -------- #

        elif "open google" in command:
            open_google()

        elif "close google" in command:
            os.system("taskkill /im chrome.exe /f")
            print("Google closed")

        elif "open youtube" in command:
            open_youtube()

        elif "close youtube" in command:
            pyautogui.hotkey("ctrl","w")
            print("YouTube closed")

        elif "open chrome" in command:
            open_chrome()

        elif "close chrome" in command:
            os.system("taskkill /im chrome.exe /f")
            print("Chrome closed")

        # -------- OPEN FOLDER -------- #

        elif "open folder" in command:

            folder_name = command.replace("open folder","").strip()

            search_and_open(folder_name,"folder")

        # -------- OPEN FILE -------- #

        elif "open file" in command:

            file_name = command.replace("open file","").strip()

            search_and_open(file_name,"file")

        # -------- CLOSE WINDOW -------- #

        elif "close window" in command:

            pyautogui.hotkey("alt","f4")

            print("Window closed")

        else:

            print("Command not recognized")

    except sr.UnknownValueError:

        print("Could not understand voice")

    except sr.RequestError:

        print("Speech service unavailable")

    except Exception as e:

        print("Error:", e)