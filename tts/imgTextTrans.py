from ctypes.wintypes import RGB
from PIL import Image
from datetime import datetime
import pytesseract
from googletrans import Translator
import cv2
import numpy as np
from gtts import gTTS
#from playsound import playsound
from preferredsoundplayer import playsound
# sharpening_mask1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
# sharpening_mask2 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])


#comment: 이미지 텍스트화
def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    for text in texts:
        return text.description


#comment: TTS
def speak(text):
    currentTime=datetime.now()
    now = currentTime.strftime("%Y%m%d-%H%M%S")
    tts = gTTS(text = text, lang = 'ko')
    path='./tts/sound/'
    filename = '{0}.mp3'.format(now)
    tts.save(path+filename)
    playsound(path+filename)

#COMMENT: 이미지 텍스트화 객체 및 언어 번역 객체
trans = Translator()

#comment: 입력 사진 path
path="./images/"
imKor = "sampleKor3.jpg"
imEn="sampleEn.jpg"

imgPathKor=path+imKor
imgPathEn=path+imEn

"""
#comment: 이미지 처리 configuration
# configKor=('-l kor --oem 3 --psm 4')        #oem 2 or 3 선택
# configEn=('-l eng --oem 2 --psm 3')         #psm 3 or 4 선택
# configs = ('-l kor+eng --oem 3 --psm 4')

#comment: 이미지 전처리
# img = imagePreprocessing(imgPathEn)
# img=imagePreprocessing(imgPathKor)

#comment: 이미지 텍스트화 및 번역
# its = pytesseract.image_to_string(img, config=configEn)
# its = pytesseract.image_to_string(img, config=configKor)
# its = pytesseract.image_to_string(img, config=configs)
"""


def transSpeak(imgPath):
    trans = Translator()
    imgToStr = detect_text(imgPath)
    lang = trans.detect(imgToStr.strip())
    if(lang.lang == 'ko'):
        print(imgToStr.strip())
        speak(imgToStr.strip())

    elif(lang.lang == 'en'):
        res = trans.translate(imgToStr.strip(), dest="ja")
        res = trans.translate(res.text.strip(), dest="ko")

        print(res.text.strip())
        speak(res.text)


def mainStart():
    # comment: 입력 사진 path
    # path="./tts/img/"
    path = "./images/"
    img = "sampleKor.jpg"

    pathImg=path+img

    transSpeak(pathImg)

mainStart()