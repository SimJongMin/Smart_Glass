from time import sleep
import os


def camera():
        os.system("libcamera-still -o ./images/captured.jpg")
