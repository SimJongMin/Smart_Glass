# 1_main 클라이언트

import os
import cv2
import sys
from matplotlib import pyplot as plt
import numpy as np
from socket import *
from datetime import datetime
from gtts import gTTS
from preferredsoundplayer import playsound
from camera import processing
from camera import resizing
from camera import camera_capture


def speak(text):
    currentTime = datetime.now()
    now = currentTime.strftime("%Y%m%d-%H%M%S")
    tts = gTTS(text=text, lang='ko')
    path = './tts/sound/'
    filename = '{0}.mp3'.format(now)
    tts.save(path+filename)
    playsound(path+filename)

# 카메라 함수
def camera1() : 
    camera = PiCamera()
    camera.start_preview()
    sleep(3)
    camera.capture("./demoImage/capture.jpg") # 경로 수정 필요
    camera.stop_preview()    

PROTOCOL = 0
num=int(sys.argv[1])

# camera1() # comment: 라즈베리파이 3에서 사용하는 촬영 코드
camera_capture.camera()    # comment: 라즈베리파이 4에서 사용하는 촬영 코드

processing.camera_processing("./demoImage/capture.jpg")
resizing.resizing(num)

img = './demoImage/Braille/resized_image.jpg'  # 여기에 카메라로 찍은 사진을 넣으면 된다.
img_size = os.path.getsize(img)

socket = socket(AF_INET, SOCK_STREAM)
socket.connect(('127.0.0.1', 9658))
print("클라이언트: 서버 접속 완료.")

socket.send(PROTOCOL.to_bytes(4, byteorder = "little"))
socket.send(img_size.to_bytes(4, byteorder = "little"))

file = open(img, "rb")
data = file.read(img_size)
socket.send(data)
file.close()
print("클라이언트: 파일 송신 완료.")

plain_text = socket.recv(1024).decode('utf-8')

socket.close()

print(plain_text)
speak(plain_text)
