# 1_main 클라이언트
import os
import sys
from socket import *
from datetime import datetime
from gtts import gTTS
from preferredsoundplayer import playsound
from camera import processing
from camera import resizing

'''
매개변수 : 점자 이미지 파일명
'''

filedic = {1: "라즈베리파이4_14.jpg", 2: "소고기입니다_11.jpg", 3: "안녕하세요_8.jpg", 4: "오늘의점심은_12.jpg", 5: "운수좋은날.jpg",
           6: "인간실격_43.jpg", 5: "점자가인식되었습니다_11.jpg", 6: "하루되세요_9.jpg", 7: "한성대학교2022캡스톤디자인_29.jpg", 8: "행복한_8.jpg"}





def speak(text):
    currentTime = datetime.now()
    now = currentTime.strftime("%Y%m%d-%H%M%S")
    tts = gTTS(text=text, lang='ko')
    path = './tts/sound/'
    filename = '{0}.mp3'.format(now)
    tts.save(path+filename)
    playsound(path+filename)

PROTOCOL = 0

key=sys.argv[1]
temp1=filedic[key].split("_")
res=temp1[1].split(".")
num=int(res)



os.system("libcamera-jpeg -o ./demoImage/capture.jpg")
processing.camera_processing("./demoImage/Braille/"+filedic[key])
resizing.resizing(num)

img="./demoImage/Braille/resized_image.jpg"
img_size = os.path.getsize(img)

socket = socket(AF_INET, SOCK_STREAM)
socket.connect(('192.168.219.108', 9658))
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


'''
이미지 파일명을 argv로 받아서 이미지를 서버에 보낸다.
'''