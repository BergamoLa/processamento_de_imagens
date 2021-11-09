import numpy as np
import random
import cv2

#carregar uma imagem
img = cv.imread("peppers.png")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

def salt_and_pepper(img,prob):
    
    output = np.zeros(img.shape,np.uint8)
    thres = 1 - prob 
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = img[i][j]
    return output

img = salt_and_pepper(img,0.05)
img1 = cv.GaussianBlur(img,(5,5),0)
img2 = cv.medianBlur(img1,9)



plt.figure(figsize=(15,15))
plt.subplot(131),plt.imshow(img),plt.title('Imagem com ruido')
plt.subplot(132),plt.imshow(img1),plt.title('GaussianBlur')
plt.subplot(133),plt.imshow(img2),plt.title('MedianBlur +GaussianBlur ')

plt.show()

