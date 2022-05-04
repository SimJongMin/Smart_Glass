

import RPi.GPIO as GPIO
from tts import imgTransCode
# from korBrailleCode import main

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def brailleCode():
    main.action()

# def transCode():
#     imgTransCode.mainStart()

transBtn=21
brailleBtn=20
btn=16

GPIO.setup(transBtn, GPIO.IN, GPIO.PUD_DOWN) # 핀 21을 입력으로 지정. 풀다운 효과 지정
GPIO.setup(brailleBtn, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(btn, GPIO.IN, GPIO.PUD_DOWN)

while True:
    btnStat=GPIO.input(transBtn)
    if(btnStat==1):
        transCode()
    
    btnStat=GPIO.input(brailleBtn)
    if(btnStat==1):
        brailleCode()
