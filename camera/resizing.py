
import cv2
import numpy as np

def resizing(num):
    img = cv2.imread('./demoImage/Braille/trimed_image.jpg')
    res = cv2.resize(img, dsize=((36*num), 42), interpolation=cv2.INTER_CUBIC)

    cv2.imwrite('./demoImage/Braille/resized_image.jpg', res)
