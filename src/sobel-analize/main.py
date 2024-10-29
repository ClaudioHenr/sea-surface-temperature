import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar as imagens representando diferentes anos
imagens = [
    cv2.imread('./assets/ocean/BMP/ocean_temp_sep_2002.bmp', cv2.IMREAD_GRAYSCALE),
    cv2.imread('./assets/ocean/BMP/ocean_temp_sep_2005.bmp', cv2.IMREAD_GRAYSCALE),
    cv2.imread('./assets/ocean/BMP/ocean_temp_sep_2008.bmp', cv2.IMREAD_GRAYSCALE),
    cv2.imread('./assets/ocean/BMP/ocean_temp_sep_2011.bmp', cv2.IMREAD_GRAYSCALE)
]

# Lista para armazenar bordas detectadas e médias das intensidades
bordas = []
medias_bordas = []

# Função para detectar bordas usando o filtro de Sobel
def detectar_bordas_sobel(imagem):
    sobel_x = cv2.Sobel(imagem, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(imagem, cv2.CV_64F, 0, 1, ksize=3)
    borda = cv2.magnitude(sobel_x, sobel_y)  # Calcular a magnitude das bordas
    return borda

# Detectar bordas e calcular média de intensidade para cada ano
for imagem in imagens:
    borda = detectar_bordas_sobel(imagem)
    bordas.append(borda)
    medias_bordas.append(np.mean(borda))  # Média das intensidades das bordas

# Exibir as imagens de borda para cada ano
fig, axs = plt.subplots(1, len(imagens), figsize=(20, 5))
anos = [2002, 2005, 2008, 2011]

for i, (borda, ano) in enumerate(zip(bordas, anos)):
    axs[i].imshow(borda, cmap='hot')
    axs[i].set_title(f'Temperaturas - Ano {ano}')
    axs[i].axis('off')

plt.show()

# Comparação e análise das variações de bordas
print("Média de Intensidade das Bordas (por Ano):")
for ano, media in zip(anos, medias_bordas):
    print(f"Ano {ano}: {media:.2f}")

# Análise final com as variações
variacoes = [medias_bordas[i] - medias_bordas[i - 1] for i in range(1, len(medias_bordas))]
print("\nVariação na Média de Intensidade das Bordas entre os Anos:")
for i in range(len(variacoes)):
    print(f"{anos[i+1]} - {anos[i]}: {variacoes[i]:.2f}")
