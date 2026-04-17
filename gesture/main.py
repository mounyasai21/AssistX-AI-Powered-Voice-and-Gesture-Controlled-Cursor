import cv2
import mediapipe as mp
import math
from gesture_control import GestureControl

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8
)

mpDraw = mp.solutions.drawing_utils

gc = GestureControl()

prev_scroll_y = 0

def fingers_up(lmList):

    fingers = []

    # thumb
    if lmList[4][0] > lmList[3][0]:
        fingers.append(1)
    else:
        fingers.append(0)

    tips = [8,12,16,20]

    for tip in tips:
        if lmList[tip][1] < lmList[tip-2][1]:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers

while True:

    success,img = cap.read()
    img = cv2.flip(img,1)

    h,w,_ = img.shape

    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    lmList = []

    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:

            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

            for id,lm in enumerate(handLms.landmark):

                cx,cy = int(lm.x*w),int(lm.y*h)
                lmList.append((cx,cy))

        if lmList:

            fingers = fingers_up(lmList)

            x,y = lmList[8]

            pinch = math.hypot(
                lmList[8][0]-lmList[4][0],
                lmList[8][1]-lmList[4][1]
            )

            # distance between index and pinky (to detect wide open hand)
            wide = math.hypot(
                lmList[8][0]-lmList[20][0],
                lmList[8][1]-lmList[20][1]
            )

            # ---------------- PRIORITY ORDER ----------------

            # 1️⃣ SELECT ALL (5 fingers wide open)
            if fingers == [1,1,1,1,1] and wide > 150:
                gc.select_all()

            # 2️⃣ SCREENSHOT (4 fingers open)
            elif fingers == [0,1,1,1,1]:
                gc.screenshot()

            # 3️⃣ TAB SWITCH
            elif fingers == [1,0,0,0,1] and wide > 120:
                gc.tab_switch()

            # 4️⃣ RIGHT CLICK
            elif fingers == [0,0,1,0,0]:
                gc.right_click()

            # 5️⃣ SCROLL
            elif fingers == [0,1,1,0,0]:

                if y < prev_scroll_y:
                    gc.scroll_up()

                elif y > prev_scroll_y:
                    gc.scroll_down()

                prev_scroll_y = y

            # 6️⃣ VOLUME
            elif fingers == [0,1,0,0,1]:

                if lmList[8][0] > lmList[20][0]:
                    gc.volume_up()
                else:
                    gc.volume_down()

            # 7️⃣ LEFT CLICK
            elif fingers[1] == 1 and pinch < 40:
                gc.left_click()

            # 8️⃣ CURSOR MOVE
            elif fingers == [0,1,0,0,0]:
                gc.move_cursor(x,y,w,h)

    cv2.imshow("Gesture Control",img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()