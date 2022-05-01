from PIL import Image
from datetime import datetime
import pytesseract
from googletrans import Translator
import cv2
from gtts import gTTS
import playsound


def imagePreprocessing(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    return img

def speak(text):
    currentTime=datetime.now()
    now = currentTime.strftime("%Y%m%d-%H%M%S")
    tts = gTTS(text = text, lang = 'ko')
    path='./tts/sound/'
    filename = '{0}.mp3'.format(now)
    tts.save(path+filename)
    playsound.playsound(path+filename)

#COMMENT: 이미지 텍스트화 객체 및 언어 번역 객체
trans = Translator()

#comment: 입력 사진 path
path="./tts/img/"
# imKor = "sampleKor.jpg"
imKor = "sampleKor2.jpg"
imEn="sampleEn.jpg"

imgPathKor=path+imKor
imgPathEn=path+imEn

#comment: 이미지 처리 configuration
configKor=('-l kor --oem 3 --psm 4')        #oem 2 or 3 선택
configEn=('-l eng --oem 2 --psm 3')         #psm 3 or 4 선택
configs = ('-l kor+eng --oem 3 --psm 4')

#comment: 이미지 전처리
# img = imagePreprocessing(imgPathEn)
img=imagePreprocessing(imgPathKor)

#comment: 이미지 텍스트화 및 번역
# its = pytesseract.image_to_string(img, config=configEn)
# its = pytesseract.image_to_string(img, config=configKor)
its = pytesseract.image_to_string(img, config=configs)
res = trans.translate(its.strip(), dest="ko")

print(res.text)
speak(res.text)

