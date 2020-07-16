import cv2

face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#img=cv2.imread('kash.jpg')
cap=cv2.VideoCapture('HS046.mov')
ret,

while cap.isOpened():

    frame=cv2.resize(frame,(500,600))
    _,img= cap.read()
    grey=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(grey, 2, 6)

    for(x,y,w,h) in faces:
       cv2.rectangle(img, (x,y), (x+w, x+h), (0,255,0), 4)
       img=cv2.resize(img, (400,500))

    cv2.imshow('img', frame)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()