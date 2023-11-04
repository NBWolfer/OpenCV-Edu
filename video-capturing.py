import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Yakalanan görüntüyü oku
    ret, frame = cap.read()
    
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    frame = cv.transpose(frame)
    # Yakalanan görüntüyü gösterme
    cv.imshow('frame', frame)

    # Çıkmak için 'q' tuşuna bas
    if cv.waitKey(1) == ord('q'): # Burada waitKey() içine aldığı milisaniye kadar bekletme yapar.
        break

# Her şey bittiğinde, 'cap' nesnesini serbest bırak
cap.release()
cv.destroyAllWindows()