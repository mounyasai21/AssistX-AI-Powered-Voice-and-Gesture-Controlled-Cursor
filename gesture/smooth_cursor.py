import pyautogui

pyautogui.FAILSAFE = False

screen_w, screen_h = pyautogui.size()

prev_x, prev_y = 0, 0
smoothening = 5


def move_cursor(x, y, cam_w, cam_h):
    global prev_x, prev_y

    screen_x = int(x * screen_w / cam_w)
    screen_y = int(y * screen_h / cam_h)

    cur_x = prev_x + (screen_x - prev_x) / smoothening
    cur_y = prev_y + (screen_y - prev_y) / smoothening

    pyautogui.moveTo(cur_x, cur_y)

    prev_x, prev_y = cur_x, cur_y