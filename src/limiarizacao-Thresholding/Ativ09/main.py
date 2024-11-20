import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Carregar a imagem colorida
color_image = cv2.imread('./assets/other/nanachi.bmp')

# Verificar se a imagem foi carregada corretamente
if color_image is None:
    raise ValueError("Imagem não encontrada. Verifique o caminho do arquivo.")

# 2. Converter para escala de cinza
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# 3. Limiarização Adaptativa
adaptive_threshold = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
adaptive_threshold_value, _ = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# 4. Limiarização Manual (com um limiar de exemplo: 127)
manual_threshold_value = 127
_, manual_threshold = cv2.threshold(gray_image, manual_threshold_value, 255, cv2.THRESH_BINARY)
manual_threshold_value, _ = cv2.threshold(gray_image, manual_threshold_value, 255, cv2.THRESH_BINARY)

otsu_threshold_value, _ = cv2.threshold(gray_image, 0, 255, cv2.THRESH_OTSU)

# 6. Exibir as imagens e os resultados
plt.figure(figsize=(12, 6))


print(f"Otsu Threshold: {otsu_threshold_value}")
print(f"Kapur Threshold: {manual_threshold_value}")
print(f"Difference: {abs(otsu_threshold_value - manual_threshold_value)}")

# Imagem original em escala de cinza
plt.subplot(1, 4, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Original Grayscale')
plt.axis('off')

# Limiarização Adaptativa
plt.subplot(1, 4, 2)
plt.imshow(adaptive_threshold, cmap='gray')
plt.title('Adaptive Threshold')
plt.axis('off')

# Limiarização Manual
plt.subplot(1, 4, 3)
plt.imshow(manual_threshold, cmap='gray')
plt.title(f'Manual Threshold (T={manual_threshold_value})')
plt.axis('off')

plt.show()
