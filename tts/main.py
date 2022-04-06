import pytesseract as tesseract
import cv2 as cv
import googletrans
from gtts import gTTS
import playsound

def imagePreprocessing(path):
    img = cv.imread(path, cv.IMREAD_GRAYSCALE)
    _, img = cv.threshold(img, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    
    return img

def speak(text):
    path = "Convert_Picture_Text\\"  # 본인 환경에 맞게 고쳐야함. 나중에 파이로 할때는 찍은 사진이 오도록 할 예정.
    filename = "voice.mp3"  # 본인 환경에 맞게 고쳐야함. 나중에 파이로 할때는 찍은 사진이 오도록 할 예정.
    
    tts = gTTS(text = text, lang = 'ko')
    tts.save(path + filename)
    playsound.playsound(path + filename)

if __name__ == "__main__":
    translator = googletrans.Translator()
    
    path = "Convert_Picture_Text\\sample\\"  # 본인 환경에 맞게 고쳐야함. 나중에 파이로 할때는 찍은 사진이 오도록 할 예정.
    filename = "sample06.png"  # 본인 환경에 맞게 고쳐야함. 나중에 파이로 할때는 찍은 사진이 오도록 할 예정.
    img = imagePreprocessing(path + filename)
    ocr = tesseract.image_to_string(img, lang = "eng")
    res = translator.translate(ocr.strip(), dest = "ko")
    
    print("===================================================================================================")
    print("원본: " + ocr)
    print("번역: " + res.text)
    print("===================================================================================================")
    speak(res.text)