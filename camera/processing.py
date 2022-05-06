import cv2, sys
from matplotlib import pyplot as plt
import numpy as np
"""
image = cv2.imread('./images/captured.png')
image_gray = cv2.imread('./images/captured.png', cv2.IMREAD_GRAYSCALE)

b, g, r = cv2.split(image)
image2 = cv2.merge([r, g, b])

plt.imshow(image2)
plt.xticks([])
plt.yticks([])
#plt.show()

#cv2.imshow('image', image)
#cv2.imshow('image_gray', image_gray)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

blur = cv2.GaussianBlur(image_gray, ksize=(1, 1), sigmaX=0)
ret, thresh1 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)


edged = cv2.Canny(blur, 10, 250)
#cv2.imshow('Edged', edged)
#cv2.waitKey(0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
cv2.imshow('closed', closed)
cv2.waitKey(0)

contours, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
total = 0

contours_xy = np.array(contours)
contours_xy.shape

x_min, x_max = 0,0
value = list()
for i in range(len(contours_xy)):
    for j in range(len(contours_xy[i])):
        value.append(contours_xy[i][j][0][0]) #네번째 괄호가 0일때 x의 값
        x_min = min(value)
        x_max = max(value)
print(x_min)
print(x_max)
 
# y의 min과 max 찾기
y_min, y_max = 0,0
value = list()
for i in range(len(contours_xy)):
    for j in range(len(contours_xy[i])):
        value.append(contours_xy[i][j][0][1]) #네번째 괄호가 0일때 x의 값
        y_min = min(value)
        y_max = max(value)
print(y_min)
print(y_max)

x = x_min
y = y_min
w = x_max-x_min
h = y_max-y_min

img_trim = image[y:y+h, x:x+w]
cv2.imwrite('./images/trimed_image.png', img_trim)
org_image = cv2.imread('./images/trimed_image.png')
#cv2.imshow('org_image', org_image)

#cv2.waitKey(0)
#cv2.destroyAllWindows()
"""
def camera_processing() :
	image = cv2.imread('./images/captured.jpg')
	image_gray = cv2.imread('./images/captured.jpg', cv2.IMREAD_GRAYSCALE)

	b, g, r = cv2.split(image)
	image2 = cv2.merge([r, g, b])

	plt.imshow(image2)
	plt.xticks([])
	plt.yticks([])
	#plt.show()

	#cv2.imshow('image', image)
	#cv2.imshow('image_gray', image_gray)

	#cv2.waitKey(0)
	#cv2.destroyAllWindows()

	blur = cv2.GaussianBlur(image_gray, ksize=(1, 1), sigmaX=0)
	ret, thresh1 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)


	edged = cv2.Canny(blur, 10, 250)
	#cv2.imshow('Edged', edged)
	#cv2.waitKey(0)

	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
	closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
	#cv2.imshow('closed', closed)
	#cv2.waitKey(0)

	contours, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	total = 0

	contours_xy = np.array(contours)
	contours_xy.shape

	x_min, x_max = 0,0
	value = list()
	for i in range(len(contours_xy)):
		for j in range(len(contours_xy[i])):
			value.append(contours_xy[i][j][0][0]) #네번째 괄호가 0일때 x의 값
			x_min = min(value)
			x_max = max(value)
	print(x_min)
	print(x_max)
 
	# y의 min과 max 찾기
	y_min, y_max = 0,0
	value = list()
	for i in range(len(contours_xy)):
		for j in range(len(contours_xy[i])):
			value.append(contours_xy[i][j][0][1]) #네번째 괄호가 0일때 x의 값
			y_min = min(value)
			y_max = max(value)
	print(y_min)
	print(y_max)

	x = x_min
	y = y_min
	w = x_max-x_min
	h = y_max-y_min

	img_trim = image[y:y+h, x:x+w]
	cv2.imwrite('./images/trimed_image.jpg', img_trim)
	# org_image = cv2.imread('./images/trimed_image.jpg')
	# cv2.imshow('org_image', org_image)

	# cv2.waitKey(0)
	# cv2.destroyAllWindows()



# camera_processing()