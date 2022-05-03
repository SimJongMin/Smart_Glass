from ctypes.wintypes import RGB
from PIL import Image
from datetime import datetime
import pytesseract
from googletrans import Translator
import cv2
import numpy as np
from gtts import gTTS
import playsound

sharpening_mask1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
sharpening_mask2 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])



def imagePreprocessing(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    
    # img=cv2.filter2D(img, -1, sharpening_mask2)
    # cv2.imshow("sharping2",img)
    # cv2.waitKey()  
    
    # kernel1=cv2.getStructuringElement((cv2.MORPH_ELLIPSE),(3,3))
    kernel2=cv2.getStructuringElement((cv2.MORPH_RECT),(2,2))

    
    # img = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel2)  #gradient연산(팽창-침식)
    
    # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 5)    #threadhold(이미지 바이너리화)
    
    _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)    #threadhold(이미지 바이너리화)
    # img=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel2)     #close연산
    # img=cv2.filter2D(img, -1, sharpening_mask1)         #이미지 샤프닝
    # img=cv2.dilate(img,kernel2)   #팽창
    # img = cv2.erode(img, kernel2)     #침식
    cv2.imshow("sharping2",img)
    cv2.waitKey()
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
imKor = "sampleKor3.jpg"
# imKor = "sampleKor2.jpg"
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
lang = trans.detect(its.strip())
if(lang.lang=='ko'):
    print(its.strip())
    # speak(its.strip())

elif(lang.lang=='en'):
    res = trans.translate(its.strip(), dest="ja")
    res = trans.translate(res.text.strip(), dest="ko")
    
    print(res.text)
    # speak(res.text)