#importação do módulo OpenCV
import cv2 as cv

#importação do módulo MatPlotLib para visualização das imagens
import matplotlib.pyplot as plt

#carregar uma imagem
img = cv.imread("peppers.png")

#converter uma imagem BGR para RGB

img1 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img1 = cv.add(img1, 100)
img1 = cv.equalizeHist(img1)
hist1 = cv.calcHist([img1],[0],None,[256],[0,255])

img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img2 = cv.subtract(img2, 100)
img2 = cv.equalizeHist(img2)
hist2 = cv.calcHist([img2],[0],None,[256],[0,255])


plt.figure(figsize=(20,15))
plt.subplot(441),plt.imshow(img1, cmap='gray'),plt.title('Mais Clara')
plt.subplot(442), plt.plot(hist1,'-',color='blue'), plt.xlim(0,255),plt.ylim(0,max(hist1)+100),plt.title('Mais Clara')
plt.subplot(443),plt.imshow(img2, cmap='gray'),plt.title('Mais Escura')
plt.subplot(444), plt.plot(hist2,'-',color='Red'), plt.xlim(0,255),plt.ylim(0,max(hist1)+100),plt.title('Mais Escura')
plt.show()