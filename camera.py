import numpy as np
import cv2 as cv

def rotate_image(image, angle):
    height, width = image.shape[:2]
    center = (width / 2, height / 2)
    
    M = cv.getRotationMatrix2D(center, angle, 1.0)

    rotated_image = cv.warpAffine(image, M, (width, height), flags=cv.INTER_LINEAR)
    
    return rotated_image

def run():
    cap = cv.VideoCapture(0)

    width = 320
    height = 240

    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()

    angle = 0 

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Não consegui capturar frame!")
            break

        frame = cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)
        image = frame.astype(float) / 255  

        rotated_image = rotate_image(image, angle)

        rotated_image = np.clip(rotated_image * 255, 0, 255).astype(np.uint8)

        cv.imshow('Imagem Rotacionada!', rotated_image)

        angle += 1

        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

run()
