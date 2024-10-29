import cv2

import barrelImg

# Carregar imagem
# image = cv2.imread('image.jpg', 0)
image = barrelImg.image

# Aplicar operador Laplaciano
laplacian = cv2.Laplacian(image, cv2.CV_64F)

cv2.imshow('Laplacian', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
