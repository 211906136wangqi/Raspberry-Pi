import cv2
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX


def close_cam():
    cap.release()
    cv2.destroyAllWindows()


def take_picture1():
    count = 1
    user_id = input("input user id:\n")
    while True:
        ok, img = cap.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(32, 32)
        )

        for(x, y, w, h) in faces:
            #        cv2.putText(img, 'yu', (x+5, y-5), font, 1, (0, 0, 255), 2)
            cv2.imwrite("./Facedata/User"+'.'+user_id+'.' +
                        str(count) + ".jpg", gray[y:y+h, x:x+w])
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
            count += 1
        if count == 101:
            break

        cv2.imshow('video', img)
        cv2.waitKey(10)
