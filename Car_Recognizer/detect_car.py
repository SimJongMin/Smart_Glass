import cv2
import os

def drawCars(img, cars):
	for (x,y,w,h) in cars:
	    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

def carRecognize(image_path):
	model_path = os.path.dirname(os.path.abspath(__file__)) + "/model/"
	# image_path = os.path.dirname(os.path.abspath(__file__)) + "/image/"

	img = cv2.imread(image_path)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	car_cascade = cv2.CascadeClassifier(model_path + 'haarcascade_car_plate.xml')

	cars = car_cascade.detectMultiScale(gray, 1.1, 5)
	return len(cars)
	# if len(cars) > 0:
    # 		print("인식됨.")
	# else:
	# 	print("인식되지 않음.")

	# drawCars(img, cars)
	# cv2.imshow("window", img)
	# if cv2.waitKey(0) & 0xFF == ord('q'):
	# 	cv2.destroyAllWindows()