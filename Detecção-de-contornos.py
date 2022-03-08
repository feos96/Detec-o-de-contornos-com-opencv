{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "83012498",
   "metadata": {},
   "outputs": [
    {
     "ename": "error",
     "evalue": "OpenCV(4.5.3) :-1: error: (-5:Bad argument) in function 'imshow'\n> Overload resolution failed:\n>  - imshow() takes at most 2 arguments (3 given)\n>  - imshow() takes at most 2 arguments (3 given)\n>  - imshow() takes at most 2 arguments (3 given)\n",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31merror\u001b[0m                                     Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_12944/966945052.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     31\u001b[0m    \u001b[1;31m#     break\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     32\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 33\u001b[1;33m \u001b[0mcv2\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mimshow\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Original'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mret\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mframe\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     34\u001b[0m \u001b[0mcv2\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwaitKey\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     35\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31merror\u001b[0m: OpenCV(4.5.3) :-1: error: (-5:Bad argument) in function 'imshow'\n> Overload resolution failed:\n>  - imshow() takes at most 2 arguments (3 given)\n>  - imshow() takes at most 2 arguments (3 given)\n>  - imshow() takes at most 2 arguments (3 given)\n"
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "\n",
    "#Gerando a função\n",
    "\n",
    "image = cv2.imread('gato.png')\n",
    "\n",
    "def sketch(image):\n",
    "    #Convertendo a imagem em escala de cinza\n",
    "    img_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)\n",
    "    \n",
    "    #Limpando a imagem com Gaussian Blur\n",
    "    img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)\n",
    "    \n",
    "    #Extraindo edges\n",
    "    canny_edges = cv2.Canny(img_gray_blur, 10, 70)\n",
    "    \n",
    "    #Inverção binaria da imagem\n",
    "    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)\n",
    "    return mask\n",
    "    \n",
    "# Inicialize a webcam e capitura o objeto fornecido pelo VideoCapture\n",
    "# Contém um booleano indicando se foi bem sucedido (ret)\n",
    "# Também contém as imagens coletadas da webcam (frame)    \n",
    "#cap = cv2.VideoCapture(0)\n",
    "\n",
    "#while True:\n",
    " #   ret, frame = cap.read()\n",
    "  #  cv2.imshow('Our Live Sketcher', sketch(frame))\n",
    "  #  if cv2.waitKey(1) == 13: #13 aperte a tecla Enter\n",
    "   #     break\n",
    "\n",
    "cv2.imshow('Original' frame)\n",
    "cv2.waitKey()\n",
    "        \n",
    "# Fecha a camera e a janela\n",
    "cap.release()\n",
    "cv2.destroyAllWindows() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b3faa89",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
