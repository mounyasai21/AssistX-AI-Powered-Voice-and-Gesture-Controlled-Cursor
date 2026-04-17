import subprocess
import sys
import os

print("AssistX Mode Controller Running")

base_dir = os.path.dirname(os.path.abspath(__file__))

voice_script = os.path.join(base_dir, "voice", "voice_control.py")
gesture_script = os.path.join(base_dir, "gesture", "main.py")

voice_process = None
gesture_process = None

while True:

    cmd = input("Enter command (voice / gesture / stop voice / stop gesture / exit): ").lower()

    # START VOICE
    if cmd == "voice":

        if voice_process is None or voice_process.poll() is not None:

            voice_process = subprocess.Popen([sys.executable, voice_script])

            print("Voice control started")

        else:
            print("Voice already running")


    # START GESTURE
    elif cmd == "gesture":

        if gesture_process is None or gesture_process.poll() is not None:

            gesture_process = subprocess.Popen([sys.executable, gesture_script])

            print("Gesture control started")

        else:
            print("Gesture already running")


    # STOP VOICE
    elif cmd == "stop voice":

        if voice_process and voice_process.poll() is None:

            voice_process.terminate()
            voice_process = None
            print("Voice control stopped")

        else:
            print("Voice is not running")


    # STOP GESTURE
    elif cmd == "stop gesture":

        if gesture_process and gesture_process.poll() is None:

            gesture_process.terminate()
            gesture_process = None
            print("Gesture control stopped")

        else:
            print("Gesture is not running")


    # EXIT PROJECT
    elif cmd == "exit":

        print("Exiting AssistX")

        if voice_process and voice_process.poll() is None:
            voice_process.terminate()

        if gesture_process and gesture_process.poll() is None:
            gesture_process.terminate()

        break


    else:
        print("Invalid command")