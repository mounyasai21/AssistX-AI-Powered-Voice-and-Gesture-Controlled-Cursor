import pyautogui
import keyboard
import time
import os

class GestureControl:

    def __init__(self):
        self.screen_w, self.screen_h = pyautogui.size()
        self.last_click = 0
        self.last_screenshot = 0

        # create screenshot folder
        self.folder = "gesture_screenshot"
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    # ---------------- CURSOR MOVE ----------------
    def move_cursor(self, x, y, cam_w, cam_h):

        screen_x = self.screen_w * x / cam_w
        screen_y = self.screen_h * y / cam_h

        pyautogui.moveTo(screen_x, screen_y)

    # ---------------- LEFT CLICK ----------------
    def left_click(self):

        if time.time() - self.last_click > 0.5:
            pyautogui.click()
            self.last_click = time.time()

    # ---------------- RIGHT CLICK ----------------
    def right_click(self):
        pyautogui.rightClick()

    # ---------------- SCROLL ----------------
    def scroll_up(self):
        pyautogui.scroll(200)

    def scroll_down(self):
        pyautogui.scroll(-200)

    # ---------------- VOLUME ----------------
    def volume_up(self):
        keyboard.send("volume up")

    def volume_down(self):
        keyboard.send("volume down")

    # ---------------- TAB SWITCH ----------------
        # ---------------- TAB SWITCH ----------------
    def tab_switch(self):

        if not hasattr(self, "last_tab"):
            self.last_tab = 0

        if time.time() - self.last_tab > 1.5:
            pyautogui.hotkey('alt','tab')
            self.last_tab = time.time()
    # ---------------- SELECT ALL ----------------
    def select_all(self):
        pyautogui.hotkey('ctrl','a')

    # ---------------- SCREENSHOT ----------------
    def screenshot(self):

        if time.time() - self.last_screenshot > 2:

            filename = f"{self.folder}/screenshot_{int(time.time())}.png"
            pyautogui.screenshot(filename)

            print("Screenshot saved:", filename)

            self.last_screenshot = time.time()