import cv2
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)


cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
fontColor = (255, 255, 255)


while True:
    ret,im=cap.read()
    gray= cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(conf<50):
            if(Id==1):
                Id="Rishabh"
            else:
                Id="Unknown"
        cv2.putText(im,str(Id), (x,y+h),font, fontScale,fontColor)
    cv2.imshow('im',im) 
    if cv2.waitKey(0):
        break
cap.release()
cv2.destroyAllWindows()