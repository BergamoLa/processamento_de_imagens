import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread('pista.jpg')
img2 = img1.copy()

img2 = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
img2 = cv.Canny(img2,500,200)

#
# Transformada de Hough
#
p1 = 250   # linhas menores que 100 pixels serão descartadas
p2 = 45    # gap com no máximo 50 pixels

linhas = cv.HoughLinesP(img2,1,np.pi/180,50,minLineLength=p1,maxLineGap=p2)

img3 = img1.copy()
if linhas is not None:
  print("Qtde linhas encontradas: %i" %(len(linhas)))

  #exibir as linhas na img 3 
  for linha in linhas:
    x1,y1,x2,y2 = linha[0]
    cv.line(img3,(x1,y1),(x2,y2),(255,0,0),3)
else:
  print("Nenhuma linha encontrada.")

plt.figure(figsize=(15,15))
plt.subplot(131), plt.imshow(img1)
plt.subplot(132), plt.imshow(img2, cmap='gray')
plt.subplot(133), plt.imshow(img3)
plt.show()