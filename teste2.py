import cv2
from ultralytics import YOLO

modelo = YOLO("yolo11n.pt")
webcam = cv2.VideoCapture(0)

if webcam.isOpened():
    validacao, frame = webcam.read()

    while validacao:
        validacao, frame = webcam.read()

        if not validacao:
            break

        resultado = modelo(frame)

        for item in resultado:
            for caixa in item.boxes:
                coordenadas = caixa.xyxy[0]

                x1 = int(coordenadas[0])
                y1 = int(coordenadas[1])
                x2 = int(coordenadas[2])
                y2 = int(coordenadas[3])

                centro_x = int((x1 + x2) / 2)
                centro_y = int((y1 + y2) / 2)

                confianca = float(caixa.conf[0])
                classe = int(caixa.cls[0])
                nome = modelo.names[classe]

                texto = nome + " " + str(round(confianca, 2))

                if confianca > 0.5:
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                    cv2.putText(
                        frame,
                        texto,
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 0),
                        2
                    )

                    cv2.circle(frame, (centro_x, centro_y), 5, (0, 0, 255), -1)

        cv2.imshow("Video da Webcam", frame)

        key = cv2.waitKey(5)

        if key == 27:  # ESC
            break

webcam.release()
cv2.destroyAllWindows()