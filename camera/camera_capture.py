import os


def camera():
        os.system("libcamera-still -o ./demoImage/capture.jpg")
