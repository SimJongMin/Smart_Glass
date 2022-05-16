# 2_main 클라이언트

import os
from socket import *
from datetime import datetime
from gtts import gTTS
from preferredsoundplayer import playsound


def speak(text):
    currentTime = datetime.now()
    now = currentTime.strftime("%Y%m%d-%H%M%S")
    tts = gTTS(text=text, lang='ko')
    path = './tts/sound/'
    filename = '{0}.mp3'.format(now)
    tts.save(path+filename)
    playsound(path+filename)


PROTOCOL = 1

img = './demoImage/tts/sampleKor.jpg'  # 여기에 카메라로 찍은 사진을 넣으면 된다.
img_size = os.path.getsize(img)

socket = socket(AF_INET, SOCK_STREAM)
socket.connect(('192.168.219.103', 9658))
print("클라이언트: 서버 접속 완료.")

socket.send(PROTOCOL.to_bytes(4, byteorder = "little"))
socket.send(img_size.to_bytes(4, byteorder = "little"))

file = open(img, "rb")
data = file.read(img_size)
socket.send(data)
file.close()
print("클라이언트: 파일 송신 완료.")

plain_text = socket.recv(65536).decode('utf-8')

socket.close()

print(plain_text)
speak(plain_text)