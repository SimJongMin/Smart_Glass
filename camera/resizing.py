
import cv2
import numpy as np

def resizing():
    img = cv2.imread('./images/trimed_image.jpg')
    res = cv2.resize(img, dsize=(324, 42), interpolation=cv2.INTER_CUBIC)

    cv2.imwrite('./images/resized_image.jpg', res)