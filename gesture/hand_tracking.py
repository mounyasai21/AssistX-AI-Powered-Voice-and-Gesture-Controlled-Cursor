import cv2
import mediapipe as mp

class HandTracking:

    def __init__(self):

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            model_complexity=1,          # better accuracy
            min_detection_confidence=0.8,
            min_tracking_confidence=0.8
        )

        self.mpDraw = mp.solutions.drawing_utils
        self.results = None


    def findHands(self, img):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:

            for handLms in self.results.multi_hand_landmarks:

                self.mpDraw.draw_landmarks(
                    img,
                    handLms,
                    self.mpHands.HAND_CONNECTIONS
                )

        return img


    def findPosition(self, img):

        lmList = []

        if self.results and self.results.multi_hand_landmarks:

            hand = self.results.multi_hand_landmarks[0]

            h, w, _ = img.shape

            for id, lm in enumerate(hand.landmark):

                cx, cy = int(lm.x * w), int(lm.y * h)

                lmList.append([id, cx, cy])

        return lmList