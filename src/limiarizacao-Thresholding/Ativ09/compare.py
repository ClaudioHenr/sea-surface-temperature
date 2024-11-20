import cv2
import matplotlib.pyplot as plt

# Carrega a imagem e converte para tons de cinza
image = cv2.imread('./assets/other/nanachi.bmp')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Limiarização de Otsu
_, otsu_thresholded = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
otsu_value = _  # Limiar calculado por Otsu

# Limiarização Binária Manual
manual_threshold_value = 127  # Valor de limiar manual (ajuste conforme necessário)
_, manual_thresholded = cv2.threshold(gray_image, manual_threshold_value, 255, cv2.THRESH_BINARY)

# Exibe as imagens e os limiares
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(gray_image, cmap='gray')
plt.title("Imagem Original em Cinza")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(otsu_thresholded, cmap='gray')
plt.title(f"Limiarização de Otsu\n(Limiar = {otsu_value})")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(manual_thresholded, cmap='gray')
plt.title(f"Limiarização Binária Manual\n(Limiar = {manual_threshold_value})")
plt.axis("off")

plt.show()
