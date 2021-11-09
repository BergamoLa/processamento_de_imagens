import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread('laranjas.jpg')
img1 = cv.cvtColor(img1,cv.COLOR_BGR2RGB)
img2 = img1.copy()

img2 = cv.cvtColor(img2,cv.COLOR_RGB2GRAY)
img2 = cv.medianBlur(img2,5)


#
# Transformada de Hough
#
circulos = cv.HoughCircles(img2,cv.HOUGH_GRADIENT, 12, 320, param1 = 200, param2 = 40, minRadius=50, maxRadius=250)
circulos = np.uint32(np.around(circulos))

img3 = img1.copy()
if circulos is not None:
  print('Qtde de laranjas encontradas: %i' %(len(circulos[0,:])))

  for circulo in circulos[0,:]:
    cv.circle(img3, (circulo[0],circulo[1]),circulo[2],(0,0,255),3)


plt.figure(figsize=(15,15))
plt.subplot(131), plt.imshow(img1)
plt.subplot(132), plt.imshow(img2, cmap='gray')
plt.subplot(133), plt.imshow(img3)
plt.show()