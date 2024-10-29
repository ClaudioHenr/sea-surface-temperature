import cv2
import matplotlib.pyplot as plt

# Carregar e converter a imagem para HSV
imagem = cv2.imread('./assets/ocean/ocean_temp_sep_2002.jpeg')
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Dividir os canais H, S e V
hue, saturation, value = cv2.split(hsv)

# Exibir os canais individualmente
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.imshow(hue, cmap='hsv')
plt.title('Hue (Matiz)')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(saturation, cmap='gray')
plt.title('Saturation (Saturação)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(value, cmap='gray')
plt.title('Value (Brilho)')
plt.axis('off')

plt.show()
