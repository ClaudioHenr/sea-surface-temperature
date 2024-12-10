import cv2
import numpy as np
import matplotlib.pyplot as plt

# Função para processar e analisar uma imagem
def processar_imagem(image_path, ano):
    # 1. Carregar a imagem de satélite
    imagem = cv2.imread(image_path)

    # 2. Converter imagem para cinza
    grayImage = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # 3. Aplica filtro Gaussiano
    blurred = cv2.GaussianBlur(grayImage, (5, 5), 0)

    # 4. Aplicar o threhold de OTSU
    _, otsu_thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Mostrar a imagem convertida após OTSU
    imageTitle = "Imagem OTSU - " + ano
    cv2.imshow(imageTitle, otsu_thresh)
    cv2.waitKey(0)  # Espera uma tecla para continuar
    cv2.destroyAllWindows()  # Fecha a janela após a visualização

    # 5. Destaca os oceanos nas imagens
    mask = cv2.bitwise_not(otsu_thresh)
    ocean_only = cv2.bitwise_and(imagem, imagem, mask=otsu_thresh)
    
    # Mostrar resultados
    imageTitle = "Imagem com oceanos destacados - " + ano
    cv2.imshow(imageTitle, ocean_only)
    cv2.waitKey(0)  # Espera uma tecla para continuar
    cv2.destroyAllWindows()  # Fecha a janela após a visualização

    # 6. Converter para o espaço de cores HSV
    hsv = cv2.cvtColor(ocean_only, cv2.COLOR_BGR2HSV)
    
    # Mostrar a imagem convertida em HSV
    imageTitle = "Imagem em HSV - " + ano
    cv2.imshow(imageTitle, hsv)
    cv2.waitKey(0)  # Espera uma tecla para continuar
    cv2.destroyAllWindows()  # Fecha a janela após a visualização
    
    # 7. Definir intervalos de cor para análise (ajustar conforme necessário)
    azul_baixo = np.array([90, 50, 50])    # Temperaturas frias
    azul_alto = np.array([130, 255, 255])
    
    branco_baixo = np.array([0, 0, 200])   # Temperaturas intermediárias
    branco_alto = np.array([180, 30, 255])
    
    vermelho_baixo = np.array([0, 50, 50]) # Temperaturas quentes
    vermelho_alto = np.array([10, 255, 255])
    
    # 8. Criar máscaras para as cores
    mascara_azul = cv2.inRange(hsv, azul_baixo, azul_alto)
    mascara_branco = cv2.inRange(hsv, branco_baixo, branco_alto)
    mascara_vermelho = cv2.inRange(hsv, vermelho_baixo, vermelho_alto)
    
    # 9. Calcular a quantidade de pixels para cada faixa de cor
    azul_pixels = cv2.countNonZero(mascara_azul)
    branco_pixels = cv2.countNonZero(mascara_branco)
    vermelho_pixels = cv2.countNonZero(mascara_vermelho)
    
    # 10. Retornar os resultados
    return azul_pixels, branco_pixels, vermelho_pixels

# Processar as imagens de diferentes anos
anos = ["2002", "2005", "2008", "2011"]
resultados = []

for ano in anos:
    caminho = f"./assets/ocean/BMP/ocean_temp_sep_{ano}.bmp"  # Ajustar os caminhos das imagens
    resultado = processar_imagem(caminho, ano)
    resultados.append(resultado)

# 11. Visualizar e comparar os resultados
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
