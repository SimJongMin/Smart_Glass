from camera import processing
from camera import resizing
from camera import camera_capture
import sys


# 카메라 함수
def camera1():
    camera = PiCamera()
    camera.start_preview()
    sleep(3)
    camera.capture("./demoImage/capture.jpg")  # 경로 수정 필요
    camera.stop_preview()


num = int(sys.argv[1])

# camera1() # comment: 라즈베리파이 3에서 사용하는 촬영 코드
camera_capture.camera()    # comment: 라즈베리파이 4에서 사용하는 촬영 코드

processing.camera_processing("./demoImage/capture.jpg")
resizing.resizing(num)



'''
카메라로 찍은 이미지를 전처리하는 과정을 보여주는 코드
'''