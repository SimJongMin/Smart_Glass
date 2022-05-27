
from Car_Recognizer import detect_car
from Car_Recognizer import detect_car
from datetime import datetime
from gtts import gTTS
from preferredsoundplayer import playsound
import cv2
import os

def speak(text):
    currentTime = datetime.now()
    now = currentTime.strftime("%Y%m%d-%H%M%S")
    tts = gTTS(text=text, lang='ko')
    path = './tts/sound/'
    filename = '{0}.mp3'.format(now)
    tts.save(path+filename)
    playsound(path+filename)
    

os.system("libcamera-jpeg -o ./demoImage/capture.jpg --width 640 --height 480")

image_path = "./demoImage/captured.jpg"
# image_path = "./Car_Recognizer/image/car01.png"


temp=cv2.imread(image_path)
cv2.imshow("sample",temp)
cv2.waitKey(0)
cv2.destroyAllWindows()

car = detect_car.carRecognize(image_path)
if car > 0:
    print("자동차가 있습니다. 조심하십시오.")
    speak("자동차가 있습니다. 조심하십시오.")
