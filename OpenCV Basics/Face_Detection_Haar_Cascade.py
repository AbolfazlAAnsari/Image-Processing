import cv2
import numpy as np


def nothing(x):
    pass

cap = cv2.VideoCapture(0)
# Need to load cascade xm5 detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cv2.namedWindow("Frame")



while True: 

    flag, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # gray image, 1 size original size, 5 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for rect in faces:
        (x, y, w, h) = rect
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    print(faces)

    cv2.imshow("Frame", frame) 

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()