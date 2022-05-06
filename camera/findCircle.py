import cv2
import sys
from matplotlib import pyplot as plt
import numpy as np


#HoughCircles를 통해 원을 잡아내는 코드 정확도는 딱히.....
# image = cv2.imread('./images/goodDay.jpg')
# image = cv2.imread('./images/testImg.jpg')
image = cv2.imread('./images/data.jpg')
dst = image.copy()


image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("figure", image)
# cv2.waitKey(0)
# image = cv2.GaussianBlur(image, (0, 0), 1)
# cimage = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1,
                           1, param1=90, param2=12, minRadius=0, maxRadius=10)
circles = np.uint16(np.around(circles))
for i in circles[0]:
    cv2.circle(dst, (i[0], i[1]), i[2], (0, 255, 0), 2)

print(circles.shape[1])
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()







#어느정도 되는 코드
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(gray, 60, 150, 3)
# cv2.imshow("figure", canny)
# cv2.waitKey(0)

dilated = cv2.dilate(canny, (1, 1), iterations=0)
# cv2.imshow("figure", dilated)
# cv2.waitKey(0)

(cnt, hierarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)

# cv2.imshow("figure", rgb)
# cv2.waitKey(0)
print("coins in the image : ", len(cnt))
print("coins in the image : ", len(cnt)//6)











# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("figure", image_gray)
# cv2.waitKey(0)


# (thresh, image_bin) = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
# cv2.imshow("figure", image_bin)
# cv2.waitKey(0)


# contours, hierarchy=cv2.findContours(image_bin, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
# for cnt in contours:
#     size=len(cnt)
#     print(size)



# blur = cv2.GaussianBlur(gray, (11, 11), 0)
# plt.imshow(blur, cmap='gray')
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# canny = cv2.Canny(blur, 30, 40, 3)
# plt.imshow(canny, cmap='gray')
# cv2.waitKey(0)


# dilated = cv2.dilate(canny, (1, 1), iterations=0) 
# plt.imshow(dilated, cmap='gray')
# cv2.waitKey(0)


# (cnt, hierarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)
# plt.imshow(rgb)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print("No of circles: ", len(cnt))
