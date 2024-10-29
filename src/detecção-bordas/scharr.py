import cv2

import barrelImg

# Carregar imagem
# image = cv2.imread('image.jpg', 0)
image = barrelImg.image

# Aplicar operador Scharr
scharrx = cv2.Scharr(image, cv2.CV_64F, 1, 0) # Bordas horizontais
scharry = cv2.Scharr(image, cv2.CV_64F, 0, 1) # Bordas verticais
scharr = cv2.sqrt(scharrx**2 + scharry**2)

cv2.imshow('Scharr', scharr)
cv2.waitKey(0)
cv2.destroyAllWindows()
