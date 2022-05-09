import cv2
import numpy as np

img=cv2.imread('./images/data2.jpg')
output=img.copy()

img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=cv2.medianBlur(img,3)

circles=cv2.HoughCircles(img,cv2.HOUGH_GRADIENT, 1,1, param1=100, param2=10, minRadius=0, maxRadius=5)

detected_circles=np.uint16(np.around(circles))


for (x,y,r) in detected_circles[0,:]:
    cv2.circle(output, (x,y), r,(0,255,0),1)
    cv2.circle(output, (x,y), 1,(0,255,0),1)

print(circles.shape[1])
cv2.imshow("output",output)
cv2.waitKey(0)
cv2.destroyAllWindows()