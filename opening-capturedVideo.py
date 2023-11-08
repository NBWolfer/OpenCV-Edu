import numpy as np
import cv2 as cv
from datetime import datetime

cap = cv.VideoCapture('./output.mp4')

print(cap.isOpened())

if not cap.isOpened():
    print("Video açılamadı")
    exit()
time = datetime.now()
while cap.isOpened():
    # fps yi ne kadar olacağını belirlemek için
    # zaman ölçme
    t1 = datetime.now()    
    ret, frame = cap.read()
    
    print(ret, frame)

    # Frame okunamadıysa, çık
    if not ret:
        print("Frame okunamadı (stream sonu?). Çıkılıyor..")
        break
    
    cv.imshow('frame', frame)
    t2 = datetime.now()
    print(t2-t1)
    if cv.waitKey(24) == ord('q'): # ölçülen zamana göre waitKey() için değer belirleme
        break
time = datetime.now() - time
print(time)
cap.release()
cv.destroyAllWindows()