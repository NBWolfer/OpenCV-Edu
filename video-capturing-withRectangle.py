import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Burada bir model ile çalışılırken dikdörtgenin ölçüleri ve konumu
    # bu modelin çıktıları ile ayarlanır
    rectangle_x, rectangle_y, rectangle_width, rectangle_height = 100, 100, 340, 280
    cv.rectangle(frame, (rectangle_x, rectangle_y), (rectangle_x+rectangle_height, rectangle_y+rectangle_width), (0, 255, 0), 2)
    cv.putText(frame, 'Rectangle', (rectangle_x, rectangle_y-10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()