#识别静态图片中的人脸,打上方框

import cv2
import os

filename = 'faceRecogMulti.jpg'


def detect(filename):
    workDir = os.getcwd()
    face_cascade = cv2.CascadeClassifier(os.path.join(workDir, 'cascades','haarcascade_frontalface_default.xml'))
    eye_cascade = cv2.CascadeClassifier(os.path.join(workDir, 'cascades','haarcascade_eye.xml' ))
    img = cv2.imread(os.path.join(workDir,filename))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.namedWindow('Faces Detected!!')
    cv2.imshow('Faces Detected!!', img)
    cv2.imwrite(os.path.join(workDir, 'Faces.jpg'), img)
    cv2.waitKey(0)

detect(filename)
