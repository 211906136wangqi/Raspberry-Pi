import os
import cv2
import numpy as np
from PIL import Image
faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')


def conversion1():
    img_path = 'Facedata'
    all_image_paths = [os.path.join(img_path, f) for f in os.listdir(img_path)]
    print(all_image_paths)

    ids = []
    face_samples = []

    for each_img in all_image_paths:
        id = int(os.path.split(each_img)[1].split('.')[1])
        PIL_img = Image.open(each_img).convert('L')
        np_img = np.array(PIL_img, 'uint8')
        faces = faceCascade.detectMultiScale(np_img)
        for(x, y, w, h) in faces:
            face_samples.append(np_img[y:y+h, x:x+w])
            ids.append(id)
