# from camera import camera_capture
# from camera import processing
# from tts import imgTextTrans
from korBrailleCode import korBrailleCNN
import main
from datetime import datetime
from gtts import gTTS
from preferredsoundplayer import playsound
# from korBrailleCode import Make_model
# from korBrailleCode import Rdy_image
# from korBrailleCode import DATAGenerator
# from korBrailleCode import divide
# from korBrailleCode import Predict
# from korBrailleCode import Load_model


# camera_capture.camera()
# processing.camera_processing()

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
# print(str)