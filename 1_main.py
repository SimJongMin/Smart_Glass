import cv2, sys
from matplotlib import pyplot as plt
import numpy as np
from camera import processing
from korBrailleCode import korBrailleCNN
from Braille_Translator import translate_braille
from datetime import datetime
from gtts import gTTS
from preferredsoundplayer import playsound
from camera import resizing



processing.camera_processing("./images/brailleTest1.jpg")
resizing.resizing()



def speak(text):
    currentTime = datetime.now()
    now = currentTime.strftime("%Y%m%d-%H%M%S")
    tts = gTTS(text=text, lang='ko')
    path = './tts/sound/'
    filename = '{0}.mp3'.format(now)
    tts.save(path+filename)
    playsound(path+filename)


for _ in range(2):
    lists=korBrailleCNN.action()                
    print(lists)
    str=translate_braille.trans(lists)
    speak(str)
    print(str)
