import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('MELANOMA2.jpg')


# CONVERTER a imagem de RGB para HSV
img1 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img2 = cv.cvtColor(img1, cv.COLOR_RGB2HSV)

#SEGMENTAÇÃO POR COR 
ini = np.array([0,95,40])            
fim = np.array([20,255,255])
img3 = cv.inRange(img2,ini,fim)
ini = np.array([0,95,50])            
fim = np.array([20,255,255])
img3 = cv.inRange(img2,ini,fim)

#determinar os contornos da imagem pós segmentação
contornos, ordem = cv.findContours(img3,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
print("Total de contornos= {0}".format(len(contornos)))

#ordenar os contornos por tamanho
contornos = sorted(contornos,key=cv.contourArea)

img4 = img3.copy()

#visualizar os contornos
cv.drawContours(img4,contornos,-1,(0,0,0), 10)


plt.figure(figsize=(20,20))
plt.subplot(331), plt.imshow(img1), plt.title('Imagem de melanoma em RGB')
plt.subplot(332), plt.imshow(img2, cmap='hsv'), plt.title('Imagem de melanoma em HSV')
plt.subplot(333), plt.imshow(img3, cmap='binary'),plt.title('Segmentação')
plt.subplot(334), plt.imshow(img4, cmap='binary'),plt.title('CANNY')
plt.show()
