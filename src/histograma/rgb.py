import cv2
import matplotlib.pyplot as plt

# Carregar a imagem em BGR (padrão do OpenCV)
imagem = cv2.imread('./assets/ocean/ocean_temp_sep_2002.jpeg')

# Separar os canais de cor BGR
canais = cv2.split(imagem)
cores = ('b', 'g', 'r')  # Definindo a sequência BGR

# Configurar o gráfico
plt.figure()
plt.title('Histograma RGB')
plt.xlabel('Intensidade de Pixel')
plt.ylabel('Número de Pixels')

# Calcular e plotar o histograma para cada canal de cor
for canal, cor in zip(canais, cores):
    hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
    plt.plot(hist, color=cor)  # Define a cor de cada canal (b, g, r)
    plt.xlim([0, 256])

# Exibir o histograma
plt.show()
