import pyautogui
import subprocess
import time
import webbrowser
import os

# ---------------- MOUSE ---------------- #

def left_click():
    pyautogui.click()

def right_click():
    pyautogui.rightClick()

def double_click():
    pyautogui.doubleClick()

def scroll_up():
    pyautogui.scroll(400)

def scroll_down():
    pyautogui.scroll(-400)


# ---------------- KEYBOARD ---------------- #

def tab_switch():
    pyautogui.hotkey("alt", "tab")

def select_all():
    pyautogui.hotkey("ctrl", "a")


# ---------------- SCREENSHOT ---------------- #

def take_screenshot():
    filename = f"screenshot_{int(time.time())}.png"
    pyautogui.screenshot(filename)
    print("Screenshot saved:", filename)


# ---------------- VOLUME ---------------- #

def volume_up():
    pyautogui.press("volumeup")

def volume_down():
    pyautogui.press("volumedown")


# ---------------- BRIGHTNESS ---------------- #

def brightness_up():
    subprocess.run(
        'powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,90)',
        shell=True
    )

def brightness_down():
    subprocess.run(
        'powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,30)',
        shell=True
    )


# ---------------- BROWSER ---------------- #

def open_google():
    webbrowser.open("https://www.google.com")

def close_google():
    os.system("taskkill /im chrome.exe /f")

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def close_youtube():
    os.system("taskkill /im chrome.exe /f")

def open_chrome():
    os.system("start chrome")

def close_chrome():
    os.system("taskkill /im chrome.exe /f")


# ---------------- FILES ---------------- #

def open_downloads():
    path = os.path.join(os.path.expanduser("~"), "Downloads")
    os.startfile(path)

def close_downloads():
    os.system("taskkill /im explorer.exe /f")