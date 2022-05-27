import time
import RPi.GPIO as GPIO
import mode2


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

mode1 = 16  # 핀 번호 21
GPIO.setup(mode1, GPIO.IN, GPIO.PUD_DOWN)  # 핀 21을 입력으로 지정. 풀다운 효과 지정

mode2 = 17  # 핀 번호 21
GPIO.setup(mode2, GPIO.IN, GPIO.PUD_DOWN)  # 핀 21을 입력으로 지정. 풀다운 효과 지정

mode3 = 18  # 핀 번호 21
GPIO.setup(mode3, GPIO.IN, GPIO.PUD_DOWN)  # 핀 21을 입력으로 지정. 풀다운 효과 지정


print("* press button *")
while True:
    str=input("input argument : ")
    
    mode=GPIO.input(mode2)
    if mode==1:
        mode2.mode2(str)
    