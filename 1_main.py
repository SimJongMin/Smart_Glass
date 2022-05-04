from camera import camera_capture
from camera import processing
from tts import imgTextTrans
from korBrailleCode import korBrailleCNN
from Braille_Translator import main




camera_capture.camera()
processing.camera_processing()

main.trans(korBrailleCNN.action())  # tts는 Braille_Translator -> main 맨 밑에 print문 지우고 그 위치에 넣으면 됨.
