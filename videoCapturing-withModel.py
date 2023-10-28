from keras.models import load_model  # TensorFlow, Keras kütüphanesinin çalışması için gereklidir
import cv2 as cv
import numpy as np

# Bilimsel notasyonu kapat, bu şekilde sayılar daha okunabilir olur
np.set_printoptions(suppress=True)

# Modeli yükle
model = load_model("./keras/keras_Model.h5", compile=False)

# Etiketleri yükle
class_names = open("./keras/labels.txt", "r").readlines()

# Kamera 0 ya da 1 numaralı cihazınız olabilir. 0 genellikle dahili kameranızdır.
camera = cv.VideoCapture(0)

while True:
    # Kamera veya başka bir kaynakla çerçeveleri yakalamaya başlayın
    ret, image = camera.read()

    image = cv.flip(image, 1)

    # Resmi yeniden boyutlandırma
    image_ = cv.resize(image, (224, 224), interpolation=cv.INTER_AREA)
    image_ = cv.flip(image_, 1)

    # Resmi model için uygun hale getir
    image_ = np.asarray(image_, dtype=np.float32).reshape(1, 224, 224, 3)

    # Resim dizisini 0 ile 1 arasında normalleştir
    image_ = (image_ / 127.5) - 1

    # Modeli kullanarak tahmin yap
    prediction = model.predict(image_)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Tahmini ve güven skorunu yazdır
    text = f"Class: {class_name[2:len(class_name)-1]}"
    text2 = f"Accuracy: {str(np.round(confidence_score * 100))[:-2]}%"
    cv.putText(image, text, (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (100, 255, 0), 2)
    cv.putText(image, text2, (10, 60), cv.FONT_HERSHEY_SIMPLEX, 1, (100, 255, 0), 2)
    print(text)
    print(image.shape)

    # Çerçeveyi göster
    cv.imshow('frame', image)

    # Klavyeden 'esc' basılırsa, çık
    keyboard_input = cv.waitKey(1)

    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        break

camera.release()
cv.destroyAllWindows()
