import cv2 as cv
import matplotlib.pyplot as plt

img1 = cv.imread("peppers.png")
img2 = cv.imread("lena.png")
img3 = cv.imread("baboon.png")



img1 = cv.cvtColor(img1, cv.COLOR_BGR2RGB)
img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
img3 = cv.cvtColor(img3, cv.COLOR_BGR2RGB)
img3 = cv.cvtColor(img3, cv.COLOR_RGB2GRAY)


#IMG3 PRETO E BRANCO
#converter RGB->Binário
for lin in range(img3.shape[0]):   
  for col in range(img3.shape[1]):
    
    pixel = img3.item(lin,col)
    if ( pixel > 127 ):
      img3.itemset( (lin,col), 255)
    else:
      img3.itemset( (lin,col), 0)

#QUANTIDADE DE PIXEL DA IMG1 
print("A quantidade de pixels da imagem 1 = ", img1.shape[0] * img1.shape[1])

#QUANTIDADE DE COLUNA DA IMG2 
print("A quantidade de linhas da imagem 2 = ", img2.shape[0])

#QUANTIDADE DE COLUNAS DA IMG3 
print("A quantidade de colunas da imagem 3 = ", img3.shape[1])

plt.figure(figsize=(14,14))
plt.subplot(131),plt.imshow(img1, cmap='gray'),plt.title('original')
plt.subplot(132),plt.imshow(img2, cmap='gray'),plt.title('IMG2 EM TONS DE CINZA')
plt.subplot(133),plt.imshow(img3, cmap='binary'),plt.title('IMG3 EM PRETO E BRANCO')
plt.show()
