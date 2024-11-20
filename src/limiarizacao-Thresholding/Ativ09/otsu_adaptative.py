import cv2
import matplotlib.pyplot as plt

# Carrega a imagem e converte para tons de cinza
image = cv2.imread('./assets/other/nanachi.bmp')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Limiarização de Otsu
_, otsu_thresholded = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Limiarização Adaptativa (usando a média dos pixels vizinhos como referência)
adaptive_thresholded = cv2.adaptiveThreshold(
    gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
)

# Exibe as imagens e os limiares
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(gray_image, cmap='gray')
plt.title("Imagem Original em Cinza")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(otsu_thresholded, cmap='gray')
plt.title("Limiarização de Otsu")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(adaptive_thresholded, cmap='gray')
plt.title("Limiarização Adaptativa")
plt.axis("off")

plt.show()
