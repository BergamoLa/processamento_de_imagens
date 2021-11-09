import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('lago.png')

# CONVERTER a imagem de RGB para HSV
img1 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img2 = cv.cvtColor(img1, cv.COLOR_RGB2HSV)

#118
ini = np.array([90,140,70])            
fim = np.array([140,255,255])
img3 = cv.inRange(img2,ini,fim)


plt.figure(figsize=(15,15))
plt.subplot(221), plt.imshow(img1, cmap='hsv'), plt.title('Lago')
plt.subplot(222), plt.imshow(img3, cmap='binary'),plt.title('Segmentação')
plt.show()