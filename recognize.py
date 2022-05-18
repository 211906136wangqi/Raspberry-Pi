import os
import cv2
import datetime
import numpy as np
from PIL import Image
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
font = cv2.FONT_HERSHEY_SIMPLEX

recognizer = cv2.face.LBPHFaceRecognizer_create()
faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')


def recognize1():
    # 加载训练好的文件 等下用来识别
    recognizer.read('people.yml')

    while True:
        ok, img = cap.read()
        id = 0
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(32, 32)
        )

        for(x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            id, con = recognizer.predict(gray[y:y+h, x:x+w])
            # if id == 136:
            #    name = 'wangqi'
            cv2.putText(img, str(id), (x+5, y-5), font, 1, (0, 0, 255), 1)

        cv2.imshow('video', img)
        img_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        key = cv2.waitKey(10)
        if key == 27:
            cv2.imwrite("./photo/" + str(id) + '-' +
                        str(img_name) + ".jpg", img)
            break
