from picamera import PiCamera
from time import sleep

"""
camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/camera/images/captured.jpg')
camera.stop_preview()
"""

def camera() :

        camera = PiCamera()

        camera.start_preview()
        sleep(5)
        camera.capture('/home/pi/camera/images/captured.jpg')
        camera.stop_preview()
