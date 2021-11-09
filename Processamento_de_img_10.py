import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('MELANOMA.jpg')

mask = np.array( [[0,-1,0],[-1,5,-1],[0,-1,0]])
img1 = cv.filter2D(img1,-1,mask)

# CONVERTER a imagem de RGB para HSV
img1 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img2 = cv.cvtColor(img1, cv.COLOR_RGB2HSV)

ini = np.array([0,150,0])            
fim = np.array([20,255,120])
img3 = cv.inRange(img2,ini,fim)

#determinar os contornos da imagem pós segmentação por cor
contornos, ordem = cv.findContours(img3,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
print("Total de contornos= {0}".format(len(contornos)))

#ordenar os contornos por tamanho
contornos = sorted(contornos,key=cv.contourArea)


img3 = cv.cvtColor(img3, cv.COLOR_GRAY2RGB)


img4 = img3.copy()
#visualizar os contornos
cv.drawContours(img4,contornos,-1,(0,0,0), 10)


plt.figure(figsize=(20,20))
plt.subplot(431), plt.imshow(img1), plt.title('Imagem de melanoma em RGB')
plt.subplot(432), plt.imshow(img2, cmap='hsv'), plt.title('Imagem de melanoma em HSV')
plt.subplot(433), plt.imshow(img3, cmap='binary'),plt.title('Segmentação por cor')
plt.subplot(434), plt.imshow(img4, cmap='binary'),plt.title('EXIBIÇÃO DOS CONTORNOS')
plt.show()
