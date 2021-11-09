import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread('pessoas.jpg')
img1 = cv.cvtColor(img1,cv.COLOR_BGR2RGB)

#
# Retângulo de Segmentação
#
img2 = img1.copy()
p1 = (100,0)
p2 = (900,800)
img2 = cv.rectangle(img2, p1, p2, (255,0,0), 2)


# Parâmetros
mascara = np.zeros(img1.shape[:2], np.uint8)  # receber o resultado do algoritmo
bgModel = np.zeros((1,65), np.float64)        # modelo background
fgModel = np.zeros((1,65), np.float64)        # modelo do foreground
retangulo = p1+p2

#
# Aplicar o Algoritmo GRABCUT
#
# cv.GC_INIT_WITH_RECT = retângulo de segmentação
# cv.GC_INIT_WITH_MASK = pixels de segmentação informados pelo usuário
cv.grabCut(img1,mascara,retangulo,bgModel,fgModel,10, cv.GC_INIT_WITH_RECT)

# Separar o Background do Foreground
# Após a execução do algoritmo, a variável mascara contém valores entre 0 e 3
# Os valores iguais a 0 (zero) ou 2 (dois) representam o Background
# Os valores iguais a 1 (um) ou 3 (três) representam o Foreground

# Filtrar os pixels de background
filtro = np.where( (mascara == 0) | (mascara == 2), 0, 1).astype('uint8')
img3 = img1.copy()
img3 = img3 * filtro[:,:,np.newaxis]


plt.figure(figsize=(20,20))
plt.subplot(131), plt.imshow(img1)
plt.subplot(132), plt.imshow(img2)
plt.subplot(133),plt.imshow(img3)

plt.show()