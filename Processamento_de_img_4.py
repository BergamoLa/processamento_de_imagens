#importação do módulo OpenCV
import cv2 as cv

#importação do módulo MatPlotLib para visualização das imagens
import matplotlib.pyplot as plt

#carregar uma imagem
img = cv.imread("peppers.png")

#converter uma imagem BGR para RGB
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img = cv.cvtColor(img, cv.COLOR_RGB2HSV)


plt.figure(figsize=(15,15))
plt.subplot(121),plt.imshow(img, cmap='hsv'),plt.title('HSV')
plt.show()