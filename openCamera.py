#打开摄像头,显示摄像头画面，按ESC退出
#By henry cinque, 20180820
import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    cv2.imshow('simple', img)
    k = cv2.waitKey(30)&0xff
    if k == 27:
        break
cap.release
cv2.destroyAllWindows()