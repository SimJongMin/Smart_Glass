import os
import cv2
import sys
from matplotlib import pyplot as plt
import numpy as np
from camera import processing
from tts import imgTextTrans
from googletrans import Translator
from preferredsoundplayer import playsound
from gtts import gTTS
from datetime import datetime


#os.system("libcamera-still -o ./camera/images/captured.jpg")
#processing.camera_processing()


#comment: TTSv
def speak(text):
    currentTime = datetime.now()
    now = currentTime.strftime("%Y%m%d-%H%M%S")
    tts = gTTS(text=text, lang='ko')
    path = './tts/sound/'
    filename = '{0}.mp3'.format(now)
    tts.save(path+filename)
    playsound(path+filename)


trans = Translator()
str = imgTextTrans.mainStart(trans)
print(str)
speak(str)