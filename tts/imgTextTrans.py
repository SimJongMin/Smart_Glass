from datetime import datetime
from googletrans import Translator
from gtts import gTTS
from preferredsoundplayer import playsound


#comment: 이미지 텍스트화
def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    import os

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "./apiKey/potent-smithy-349713-8f1ceac136e4.json"
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


def transSpeak(imgPath, trans):
    imgToStr = detect_text(imgPath)
    lang = trans.detect(imgToStr.strip())
    if(lang.lang == 'ko'):
        return imgToStr.strip()

    elif(lang.lang == 'en'):
        res = trans.translate(imgToStr.strip(), dest="ja")
        res = trans.translate(res.text.strip(), dest="ko")
        return res.text.strip()


def mainStart(trans):
    # comment: 입력 사진 path
    # path="./demoImage/"
    path = "./tts/"
    img = "sampleEn8.jpg"

    pathImg=path+img

    str=transSpeak(pathImg, trans)
    print(str)
    speak(str)
    return str

# trans=Translator()
# mainStart(trans)

def serverMainStart(trans, image):
    # comment: 입력 사진 path
    # path="./tts/img/"
    #path = "./images/

    pathImg=image

    str=transSpeak(pathImg, trans)
    return str


