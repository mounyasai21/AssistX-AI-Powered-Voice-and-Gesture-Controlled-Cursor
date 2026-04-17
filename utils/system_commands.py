import pyautogui
import webbrowser
import os
import subprocess
import time

# ---------------- MOUSE ---------------- #

def left_click():
    pyautogui.click()
    print("Left Click")

def right_click():
    pyautogui.rightClick()
    print("Right Click")

def double_click():
    pyautogui.doubleClick()
    print("Double Click")

def scroll_up():
    pyautogui.scroll(700)
    print("Scroll Up")

def scroll_down():
    pyautogui.scroll(-700)
    print("Scroll Down")

# ---------------- KEYBOARD ---------------- #

def select_all():
    pyautogui.hotkey('ctrl','a')
    print("Select All")

# ---------------- SCREENSHOT ---------------- #

def take_screenshot():

    folder = os.path.join(os.path.expanduser("~"), "Desktop")

    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = os.path.join(folder, f"screenshot_{int(time.time())}.png")

    pyautogui.screenshot(filename)

    print("Screenshot Saved:", filename)

# ---------------- VOLUME ---------------- #

def volume_up():
    pyautogui.press("volumeup")
    print("Volume Up")

def volume_down():
    pyautogui.press("volumedown")
    print("Volume Down")

# ---------------- BRIGHTNESS ---------------- #

def brightness_up():
    subprocess.run("powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,80)", shell=True)
    print("Brightness Increased")

def brightness_down():
    subprocess.run("powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,30)", shell=True)
    print("Brightness Decreased")

# ---------------- BROWSER ---------------- #

def open_google():
    webbrowser.open("https://www.google.com")
    print("Opening Google")

def close_google():
    pyautogui.hotkey("ctrl","w")
    print("Google Tab Closed")

def open_youtube():
    webbrowser.open("https://www.youtube.com")
    print("Opening YouTube")

def close_youtube():
    pyautogui.hotkey("ctrl","w")
    print("YouTube Tab Closed")

def open_chrome():
    subprocess.Popen("start chrome", shell=True)
    print("Opening Chrome")

def close_chrome():
    subprocess.Popen("taskkill /IM chrome.exe /F", shell=True)
    print("Chrome Closed")

# ---------------- FOLDERS ---------------- #

def open_downloads():

    path = os.path.join(os.path.expanduser("~"), "Downloads")
    subprocess.Popen(f'explorer "{path}"')

    print("Opening Downloads")

def close_downloads():

    subprocess.Popen("taskkill /IM explorer.exe /F", shell=True)
    print("Downloads Closed")
