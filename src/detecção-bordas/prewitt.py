import cv2
import numpy as np

import barrelImg

# Carregar a imagem em escala de cinza
# image = cv2.imread('image.jpg', 0)
image = barrelImg.image

# Definir as máscaras de Prewitt para os eixos x e y
prewitt_x = np.array([[1, 0, -1],
                      [1, 0, -1],
                      [1, 0, -1]])

prewitt_y = np.array([[1, 1, 1],
                      [0, 0, 0],
                      [-1, -1, -1]])

# Aplicar as máscaras usando a função filter2D do OpenCV
bordas_x = cv2.filter2D(image, cv2.CV_32F, prewitt_x)  # Converte para float32
bordas_y = cv2.filter2D(image, cv2.CV_32F, prewitt_y)  # Converte para float32

# Calcular a magnitude da borda combinada e converter de volta para uint8
bordas = cv2.magnitude(bordas_x, bordas_y).astype(np.uint8)

# Exibir os resultados
cv2.imshow("Original", image)
cv2.imshow("Bordas Prewitt - X", cv2.convertScaleAbs(bordas_x))  # Exibe em escala absoluta
cv2.imshow("Bordas Prewitt - Y", cv2.convertScaleAbs(bordas_y))  # Exibe em escala absoluta
cv2.imshow("Bordas Prewitt", bordas)

cv2.waitKey(0)
cv2.destroyAllWindows()
