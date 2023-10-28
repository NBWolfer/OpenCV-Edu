import numpy as np
import cv2 as cv

cap = cv.VideoCapture('./output.mp4')

print(cap.isOpened())

if not cap.isOpened():
    print("Video açılamadı")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    
    print(ret, frame)

    # Frame okunamadıysa, çık
    if not ret:
        print("Frame okunamadı (stream sonu?). Çıkılıyor..")
        break
    
    cv.imshow('frame', frame)
    
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()