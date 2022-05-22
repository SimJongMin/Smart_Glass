from camera import camera_capture
from Car_Recognizer import detect_car
from Car_Recognizer import detect_car
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
    
    
camera_capture.camera()
image_path = "./images/captured.jpg"

car = detect_car.carRecognize(image_path)
if car > 0:
    speak("자동차가 있습니다. 조심하십시오.")
