import cv2
import numpy as np
import matplotlib.pyplot as plt

# Função para processar e analisar uma imagem
def processar_imagem(image_path):
    # 1. Carregar a imagem de satélite
    imagem = cv2.imread(image_path)
    
    # 2. Converter para o espaço de cores HSV
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    
    # 3. Definir intervalos de cor para análise (ajustar conforme necessário)
    azul_baixo = np.array([90, 50, 50])    # Temperaturas frias
    azul_alto = np.array([130, 255, 255])
    
    branco_baixo = np.array([0, 0, 200])   # Temperaturas intermediárias
    branco_alto = np.array([180, 30, 255])
    
    vermelho_baixo = np.array([0, 50, 50]) # Temperaturas quentes
    vermelho_alto = np.array([10, 255, 255])
    
    # 4. Criar máscaras para as cores
    mascara_azul = cv2.inRange(hsv, azul_baixo, azul_alto)
    mascara_branco = cv2.inRange(hsv, branco_baixo, branco_alto)
    mascara_vermelho = cv2.inRange(hsv, vermelho_baixo, vermelho_alto)
    
    # 5. Calcular a quantidade de pixels para cada faixa de cor
    azul_pixels = cv2.countNonZero(mascara_azul)
    branco_pixels = cv2.countNonZero(mascara_branco)
    vermelho_pixels = cv2.countNonZero(mascara_vermelho)
    
    # 6. Retornar os resultados
    return azul_pixels, branco_pixels, vermelho_pixels

# Processar as imagens de diferentes anos
anos = ["2002", "2005", "2008", "2011"]
resultados = []

for ano in anos:
    caminho = f"./assets/ocean/ocean_temp_sep_{ano}.jpeg"  # Ajustar os caminhos das imagens
    resultado = processar_imagem(caminho)
    resultados.append(resultado)

# 7. Visualizar e comparar os resultados
azul_vals, branco_vals, vermelho_vals = zip(*resultados)

plt.figure(figsize=(10, 6))
plt.plot(anos, azul_vals, label='Frio (Azul)', marker='o', color='blue')
plt.plot(anos, branco_vals, label='Intermediário (Branco)', marker='o', color='gray')
plt.plot(anos, vermelho_vals, label='Quente (Vermelho)', marker='o', color='red')
plt.xlabel('Ano')
plt.ylabel('Quantidade de Pixels')
plt.title('Análise de Temperaturas Oceânicas ao Longo dos Anos')
plt.legend()
plt.grid(True)
plt.show()
