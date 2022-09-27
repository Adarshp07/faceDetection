

import cv2
cascade_face   = cv2.CascadeClassifier('import/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    print(ret)
    g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    f = cascade_face.detectMultiScale(g, 1.5, 1)


    for (x, y, w, h) in f:
        cv2.rectangle(img, (x, y), (x + w, y + h), (200, 356, 356), 1)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

