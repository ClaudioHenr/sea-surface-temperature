import cv2
import matplotlib.pyplot as plt

# Carregar a imagem em BGR
# imagem = cv2.imread('./assets/ocean/ocean_temp_sep_2002.jpeg')
imagem = cv2.imread('./assets/ocean/HSV/Imagem_em_HSV_2002.png')

# Converter a imagem para o espaço de cores HSV
imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Separar os canais de cor HSV
h, s, v = cv2.split(imagem_hsv)
canais = [h, s, v]
nomes = ['Hue', 'Saturation', 'Value']
cores = ['orange', 'green', 'blue']

# Configurar o gráfico
plt.figure(figsize=(10, 6))
plt.suptitle('Histograma HSV')

# Loop para calcular e plotar o histograma de cada canal HSV
for i, (canal, nome, cor) in enumerate(zip(canais, nomes, cores)):
    plt.subplot(1, 3, i+1)
    hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
    plt.plot(hist, color=cor)
    plt.title(f'{nome} Canal')
    plt.xlabel('Intensidade')
    plt.ylabel('Quantidade de Pixels')
    plt.xlim([0, 256])

# Exibir o histograma
plt.tight_layout()
plt.show()
