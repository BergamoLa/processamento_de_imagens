#importação do módulo OpenCV
import cv2 as cv

#importação do módulo MatPlotLib para visualização das imagens
import matplotlib.pyplot as plt

#carregar uma imagem
img1 = cv.imread("baboon.png")
img2 = cv.imread("lena.png")

#converter uma imagem BGR para RGB
img1 = cv.cvtColor(img1, cv.COLOR_BGR2RGB)
img2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)

#marca d'agua
img3 = cv.addWeighted(img1,0.60,img2,0.80,0)

plt.figure(figsize=(15,15))
plt.subplot(441),plt.imshow(img3),plt.title("marca d'agua")
plt.show()