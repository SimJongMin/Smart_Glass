import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound

def speak(text):
	tts = gTTS(text = text, lang = 'ko')
	filename = 'voice14.mp3'
	tts.save(filename)
#   os.getcwd()
#	time.sleep(10)
	playsound.playsound(filename)

speak("으아ㅏㅏㅏㅏ아ㄱ")
print("hello!")

