import cv2

import barrelImg

# Carregar imagem
# image = cv2.imread('image.jpg', 0)
image = barrelImg.image

# Aplicar operador Sobel
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3) # Bordas horizontais
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3) # Bordas verticais
sobel = cv2.sqrt(sobelx**2 + sobely**2)

cv2.imshow('Sobel', sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()
