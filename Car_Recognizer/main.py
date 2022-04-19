import cv2
import os

def drawCars(img, cars):
	for (x,y,w,h) in cars:
	    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

if __name__ == "__main__":
	model_path = os.path.dirname(os.path.abspath(__file__)) + "/model/"
	image_path = os.path.dirname(os.path.abspath(__file__)) + "/image/"

	img = cv2.imread(image_path + "car01.png")
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	car_cascade = cv2.CascadeClassifier(model_path + 'haarcascade_car_plate.xml')

	cars = car_cascade.detectMultiScale(gray, 1.1, 5)
	if len(cars) > 0:
		print("인식됨.")
	else:
		print("인식되지 않음.")

	drawCars(img, cars)
	cv2.imshow("window", img)
	if cv2.waitKey(0) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		
"""
자동차 번호판을 인식한다.
22 ~ 25 번째 줄은 단순한 확인용이므로, 실제 라즈베리 파이에 넣어 사용할 땐 빼도 된다.
가끔 이상한데 인식하고 자동차 라고 하는데 ㄱㅊ으려나;
"""