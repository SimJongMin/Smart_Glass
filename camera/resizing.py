from cgitb import reset
import cv2
import numpy as np

def resizing(circle_counted):
    img = cv2.imread('./images/data.jpg')
    res = cv2.resize(img, dsize=(36*circle_counted, 42), interpolation=cv2.INTER_CUBIC)

    cv2.imwrite('./images/resized_image.jpg', res)