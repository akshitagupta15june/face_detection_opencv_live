import cv2 as cv
face_cascade=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
cap=cv.VideoCapture('bts.mp4')
while cap.isOpened():
    _,img=cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eye=eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eye:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,255),5)


    cv.imshow('lovely', img)
    if cv.waitKey(1) &0xFF==ord('q'):
        break

cap.release()