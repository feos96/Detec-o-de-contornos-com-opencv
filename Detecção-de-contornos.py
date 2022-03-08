import cv2
import numpy as np

#Gerando a função
def sketch(image):
    #Convertendo a imagem em escala de cinza
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    #Limpando a imagem com Gaussian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    
    #Extraindo edges
    canny_edges = cv2.Canny(img_gray_blur, 10, 70)
    
    #Inverção binaria da imagem 
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask


#Inicialize a webcam e capitura o objeto fornecido pelo VideoCapture
#Contém um booleano indicando se foi bem sucedido (ret)
#Também contém as imagens coletadas da webcam (frame)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Our Live Sketcher', sketch(frame))
    if cv2.waitKey(1) == 13: #Aperte a tecla 13(Enter)
        break
        
#Fechando a camera e a janela
cap.release()
cv2.destroyAllWindows()      
