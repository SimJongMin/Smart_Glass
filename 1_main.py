# from camera import camera_capture
# from camera import processing
# from camera import findCircle
# from tts import imgTextTrans
from korBrailleCode import korBrailleCNN
from Braille_Translator import main
from datetime import datetime
from gtts import gTTS
from preferredsoundplayer import playsound



# camera_capture.camera()
# processing.camera_processing()
# 원 카운팅->이미지 사이즈 조정
# findCircle.findCircle()


def speak(text):
    currentTime = datetime.now()
    now = currentTime.strftime("%Y%m%d-%H%M%S")
    tts = gTTS(text=text, lang='ko')
    path = './tts/sound/'
    filename = '{0}.mp3'.format(now)
    tts.save(path+filename)
    playsound(path+filename)



lists=korBrailleCNN.action()  
print(lists)
str=main.trans(lists)
speak(str)
print(str)
