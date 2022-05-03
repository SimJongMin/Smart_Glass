#comment: google cloude 통한 이미지 글자 변환 프로그램



import io
import os
from urllib import response
from google.cloud import vision
from google.cloud.vision_v1 import types    #fixme: vision_v1사용 방법 알아보기
                                            #fixme: apiKey 환경변수 설정 확인하기

client = vision.ImageAnnotatorClient()

file_name=os.path.join(
    os.path.dirname(__file__),
    './tts/img/sampleKor.jpg'
)


with io.open(file_name, 'rb') as image_file:
    content=image_file.read()


image=types.Image(content=content)

response=client.label_detection(image=image)
labels=response.label_annotations


print("Labels : ")
for label in labels:
    print(label.description)
