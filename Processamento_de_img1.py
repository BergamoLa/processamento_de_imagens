#importação do módulo OpenCV
import cv2 as cv

#importação do módulo MatPlotLib para visualização das imagens
import matplotlib.pyplot as plt

#carregar uma imagem
img1 = cv.imread("peppers.png")
img2 = cv.imread("lena.png")
img3 = cv.imread("baboon.png")
img4 = cv.imread("airplane.png")
#converter uma imagem BGR para RGB
img1 = cv.cvtColor(img1, cv.COLOR_BGR2RGB)
img2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)
img3 = cv.cvtColor(img3, cv.COLOR_BGR2RGB)
img4 = cv.cvtColor(img4, cv.COLOR_BGR2RGB)

#operação img5 = (img1+img2)+(img3*0.5) + (img4-img1).
img5 = cv.add(cv.add(img1,img2), cv.multiply(img3,0.5), cv.subtract(img4,img1))

#img 6 not da img1
img6 = cv.bitwise_not(img1)
hist_img1 = cv.calcHist([img1],[0],None,[256],[0,255])
hist_img6 = cv.calcHist([img6],[0],None,[256],[0,255])
#visualizar a imagem
plt.figure(figsize=(15,15))
plt.subplot(441),plt.imshow(img1),plt.title('img1')
plt.subplot(442),plt.imshow(img2),plt.title('img2')
plt.subplot(443),plt.imshow(img3),plt.title('img3')
plt.subplot(444),plt.imshow(img4),plt.title('img4')
plt.subplot(445),plt.imshow(img5),plt.title('img5')
plt.subplot(446),plt.imshow(img6),plt.title('img6')
plt.subplot(447), plt.plot(hist_img1,'-',color='blue'), plt.xlim(0,255),plt.ylim(0,max(hist_img1)+100),plt.title('HISTOGRAMA DA IMAGEM 1')
plt.subplot(448), plt.plot(hist_img6,'-',color='red'), plt.xlim(0,255),plt.ylim(0,max(hist_img6)+100),plt.title('HISTOGRAMA DA IMAGEM 6')
plt.show()