import math

class Gestures:

    def distance(self, p1, p2, lmList):

        if len(lmList) < 21:
            return 999

        x1, y1 = lmList[p1][1], lmList[p1][2]
        x2, y2 = lmList[p2][1], lmList[p2][2]

        return math.hypot(x2 - x1, y2 - y1)


    def detect(self, fingers, lmList):

        if len(lmList) == 0:
            return "none"

        # pinch distance (thumb + index)
        pinch = self.distance(4, 8, lmList)

        # index finger position
        index_x = lmList[8][1]
        thumb_x = lmList[4][1]

        thumb_y = lmList[4][2]
        wrist_y = lmList[0][2]

        # ---------------- CURSOR ----------------
        if fingers == [0,1,0,0,0]:
            return "cursor"

        # ---------------- PINCH CLICK ----------------
        if pinch < 35 and fingers[1] == 1:
            return "click"

        # ---------------- RIGHT CLICK ----------------
        if fingers == [0,0,1,0,0]:
            return "right_click"

        # ---------------- DOUBLE CLICK ----------------
        if fingers == [1,1,1,0,0]:
            return "double_click"

        # ---------------- SCROLL ----------------
        if fingers == [0,1,1,0,0]:
            return "scroll"

        # ---------------- SCREENSHOT ----------------
        if fingers == [0,1,1,1,1]:
            return "screenshot"

        # ---------------- TAB SWITCH ----------------
        if fingers == [1,0,0,0,1]:
            return "tab"

        # ---------------- SELECT ALL ----------------
        if fingers == [1,1,1,1,1]:
            return "select_all"

        # ---------------- BRIGHTNESS ----------------
        if fingers == [1,0,0,0,0]:

            if thumb_y < wrist_y:
                return "brightness_up"
            else:
                return "brightness_down"

        # ---------------- VOLUME PINCH ----------------
        if pinch < 40:

            if index_x > thumb_x:
                return "volume_up"
            else:
                return "volume_down"

        return "none"