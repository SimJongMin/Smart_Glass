from picamera import PiCamera
from time import sleep

#
camera = PiCamera()

camera.start_preview()
sleep(3)
camera.capture('/home/pi/camera/images/captured.png')
camera.stop_preview()
