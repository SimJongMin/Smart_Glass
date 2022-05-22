import cv2
import numpy as np
from PIL import Image

#file_path = './korBrailleImage/'
file_name = 'a'

img = cv2.imread("./korBrailleImage/" + file_name + ".jpg")
row, col, ch = img.shape
mean = 0
var = 0.1
sigma = var**0.5
gauss = np.random.normal(mean, sigma, (row, col, ch))
gauss = gauss.reshape(row, col, ch)
noisy_array = img + gauss
noisy_image = Image.fromarray(np.uint8(noisy_array)).convert('RGB')
noisy_image.save('./noiseAdded_images/' + file_name + '_noiseadded.jpg')