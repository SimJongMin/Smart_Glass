import os
import cv2, sys
from matplotlib import pyplot as plt
import numpy as np
from camera import processing
from korBrailleCode import korBrailleCNN
from Braille_Translator import main
from datetime import datetime
from gtts import gTTS
from preferredsoundplayer import playsound
from camera import resizing


#os.system("libcamera-still -o ./camera/images/captured.jpg")
processing.camera_processing()
resizing.resizing()



def speak(text):
    currentTime = datetime.now()
    now = currentTime.strftime("%Y%m%d-%H%M%S")
    tts = gTTS(text=text, lang='ko')
    path = './tts/sound/'
    filename = '{0}.mp3'.format(now)
    tts.save(path+filename)
    playsound(path+filename)



lists=korBrailleCNN.action()                #fixme: input img를 resizing_image로 바꾸기
print(lists)
str=main.trans(lists)
speak(str)
print(str)
