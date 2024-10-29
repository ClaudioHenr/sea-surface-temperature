import cv2
import matplotlib.pyplot as plt

import barrelImg

# Carregar imagem
image = barrelImg.image

# Calcular o histograma
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# Plotar o histograma
plt.plot(hist, color='gray')
plt.title('Histograma de Intensidade')
plt.xlabel('Intensidade de Pixel')
plt.ylabel('Número de Pixels')
plt.show()
