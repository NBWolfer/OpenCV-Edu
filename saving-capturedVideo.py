import numpy as np
import cv2 as cv

# Videoyu kaydetmek için VideoWriter nesnesi oluşturun
fourcc = cv.VideoWriter_fourcc(*'H264')  # H.264 kodekini kullanın
out = cv.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))  # Video dosyasının adı ve çözünürlüğünü ayarlayın

# Kamera veya başka bir kaynakla çerçeveleri yakalamaya başlayın
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Burada çerçeveyi işleyebilirsiniz
    # Örneğin, çerçeveyi HSV'ye dönüştürmek için:
    frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Veya çerçeveyi ters çevirmek için:
    frame = cv.flip(frame, 1)

    # Çerçeveyi kaydedin
    out.write(frame)

    # Çerçeveyi göster
    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break

# Temizlik yapın ve kaynakları serbest bırakın
cap.release()
out.release()
cv.destroyAllWindows()