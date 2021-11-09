import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread('melanoma2.jpg')
img1 = cv.cvtColor(img1,cv.COLOR_BGR2RGB)


mask = np.array( [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
img2 = cv.filter2D(img1,-1,mask)

mask = np.array( [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
img2 = cv.filter2D(img2,-1,mask)


# transformar a imagem em preto/branco (binarizar)
img2 = cv.cvtColor(img1,cv.COLOR_RGB2GRAY)
th, img2 = cv.threshold(img2,1,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)


#
# morfologia matemática
#

# operação de abertura = remove pequenos ruídos da imagem
kernel = np.ones((3,3),np.uint8)    # matriz 3x3 preenchida com o valor 1 (um)
img3 = cv.morphologyEx(img2, cv.MORPH_OPEN, kernel, iterations = 5)


# operação de dilatação = preencher pequenos espaços na imagem
img4 = cv.dilate(img3, kernel, iterations=3)

#
# transformada da distância
#
# DIST_L2 = distância euclidiana
# 5       = vizinhos considerados para o cálculo da distância

img5 = cv.distanceTransform(img4, cv.DIST_L2, 3)
th, img6 = cv.threshold(img5, 0.10*img5.max(), 255, 0)

# procurar a região do watershed
img6 = np.uint8(img6)   #converter a matriz de pixels de inteiros
img7 = cv.subtract(img4,img6)

# rotular os componentes conectados da imagem
ret, rotulos = cv.connectedComponents(img6)
rotulos = rotulos + 1

# marcar a região do watershed como o valor zero
rotulos[img7 == 255] = 0    # pixels=255 são alterados para zero
img8 = cv.watershed(img1, rotulos,)
img1[rotulos == -1] = [255,0,0,]

plt.figure(figsize=(15,10))
plt.subplot(341), plt.imshow(img1)
plt.subplot(342), plt.imshow(img2,cmap='binary'),plt.title('binária')
plt.subplot(343), plt.imshow(img3,cmap='binary'),plt.title('abertura')
plt.subplot(344), plt.imshow(img4,cmap='binary'),plt.title('dilatação')
plt.subplot(345), plt.imshow(img5,cmap='gray'),plt.title('dist.transform')
plt.subplot(346), plt.imshow(img6,cmap='binary'),plt.title('dist.transform+threshold')
plt.subplot(347), plt.imshow(img7,cmap='binary'), plt.title('subtração')
plt.subplot(348), plt.imshow(img8), plt.title('resultado')

plt.show()