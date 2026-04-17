class FingerState:

    def get_fingers(self, lmList):

        fingers = [0,0,0,0,0]

        # safety check
        if not lmList or len(lmList) < 21:
            return fingers

        tipIds = [4,8,12,16,20]

        # THUMB (horizontal check)
        if lmList[4][1] > lmList[3][1]:
            fingers[0] = 1
        else:
            fingers[0] = 0

        # OTHER FINGERS (vertical check)
        for i in range(1,5):

            tip = tipIds[i]
            lower = tipIds[i] - 2

            if lmList[tip][2] < lmList[lower][2]:
                fingers[i] = 1
            else:
                fingers[i] = 0

        return fingers