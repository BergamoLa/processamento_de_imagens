#importação do módulo OpenCV
import cv2 as cv

#importação do módulo MatPlotLib para visualização das imagens
import matplotlib.pyplot as plt

#carregar uma imagem
img = cv.imread("peppers.png")

#converter uma imagem BGR para RGB
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#resize
img_bigger = cv.resize(img, (768,768)) 


print("Largura da imagem 1  = %d" %img1.shape[0])
print("Altura da imagem  1 = %d" %img1.shape[1])
print("Largura da imagem 2  = %d" %img_bigger.shape[0])
print("Altura da imagem  2 = %d" %img_bigger.shape[1])

plt.figure(figsize=(15,15))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.subplot(122),plt.imshow(img_bigger),plt.title('Aumentada')
plt.show()