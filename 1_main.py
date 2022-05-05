from camera import camera_capture
from camera import processing
from tts import imgTextTrans
from korBrailleCode import korBrailleCNN
from Braille_Translator import main




camera_capture.camera()
processing.camera_processing()

main.trans(korBrailleCNN.action())  # fixme: playsound 함수 올바르게 적용되었는지 확인



