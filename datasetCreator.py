import cv2
import numpy as np

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

id = raw_input('enter user id: ')
sample_no = 0 

while (True):
	ret, img = cam.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = faceDetect.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		sample_no = sample_no + 1 
		cv2.imwrite("dataset/User."+str(id)+"."+str(sample_no)+".jpg",gray[y:y+h, x:x+w])
		cv2.rectangle(img, (x,y),(x+w, y+h), (0,0,255), 2)
		cv2.waitKey(100)

	cv2.imshow("Face", img)
	if(sample_no > 20):
		break

cam.release()
cv2.destroyAllWindows() 
