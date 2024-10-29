import cv2
import numpy as np

import barrelImg

# Carregar imagem
image = barrelImg.image

# Definir as máscaras de Roberts para as direções x e y
roberts_x = np.array([[1, 0],
                      [0, -1]], dtype=np.float32)

roberts_y = np.array([[0, 1],
                      [-1, 0]], dtype=np.float32)

# Aplicar as máscaras usando filter2D do OpenCV
bordas_x = cv2.filter2D(image, cv2.CV_32F, roberts_x)
bordas_y = cv2.filter2D(image, cv2.CV_32F, roberts_y)

# Calcular a magnitude da borda combinada e converter de volta para uint8
bordas = cv2.magnitude(bordas_x, bordas_y).astype(np.uint8)

# Exibir os resultados
cv2.imshow("Original", image)
cv2.imshow("Bordas Roberts - X", cv2.convertScaleAbs(bordas_x))
cv2.imshow("Bordas Roberts - Y", cv2.convertScaleAbs(bordas_y))
cv2.imshow("Bordas Roberts", bordas)

cv2.waitKey(0)
cv2.destroyAllWindows()
