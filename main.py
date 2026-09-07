# bibliotecas
import cv2
from ultralytics import YOLO

modelo = YOLO("yolo11n.pt") # modelo do YOLO
webcam = cv2.VideoCapture(0) # pegar o video da webcam


if webcam.isOpened(): # abrir camera
     validacao, frame = webcam.read() # fazer validacao do frama, se der continua, se n der para
     
while validacao: 
    validacao, frame = webcam.read()
    
    if not validacao: 
            break


    resultado = modelo(frame)

    for item in resultado:
       

       for caixa in item.boxes: # fazer as coordenadas de caixa, nome, classe

        # pegar cada numero das coordenadas
        coordenadas = caixa.xyxy[0] 
        x1 = coordenadas[0]
        y1 = coordenadas[1]
        x2 = coordenadas[2]
        y2 = coordenadas[3]
        
        # pegar os xy e trasnforma em inteiros
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)

        # calcula os centros dos objetos
        centro_x = int((x1 + x2) / 2)
        centro_y = int((y1 + y2) / 2)
 
        confianca = float(caixa.conf[0])
        classe = int(caixa.cls[0])
        nome = modelo.names[classe]
        texto = nome + " " + str(round(confianca, 2))

        if confianca > 0.5:
           # desenhar caixas
           cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2) # fazer o retangulo
           cv2.putText(frame, texto, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2) # colocar a cor, texto, borda do retangulo
           cv2.circle(frame, (centro_x, centro_y), 5, (0, 0, 255), -1) # fazer um circulo no centro do objeto

    cv2.imshow("Video da Webcam", frame) # titulo 

    # FPS
    key = cv2.waitKey(5)
    if key == 27: # ESQ para parar
        break

webcam.release()
cv2.destroyAllWindows()