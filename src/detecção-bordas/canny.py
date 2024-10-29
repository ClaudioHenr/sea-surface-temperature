import cv2

import barrelImg

# Carregar imagem
# image = cv2.imread('image.jpg', 0)
image = barrelImg.image

# Aplicar detecção de bordas Canny
edges = cv2.Canny(image, 100, 200)

cv2.imshow('Canny', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
