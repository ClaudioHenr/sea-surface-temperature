import cv2
import numpy as np

# Carrega a imagem colorida
color_image = cv2.imread('./assets/other/nanachi.bmp')

# Verifica se a imagem foi carregada corretamente
if color_image is None:
    raise ValueError("Imagem não encontrada. Verifique o caminho do arquivo.")

# Separa os canais B, G e R
b_channel, g_channel, r_channel = cv2.split(color_image)

# Aplica a limiarização adaptativa em cada canal individualmente
b_adaptive = cv2.adaptiveThreshold(b_channel, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 11, 2)
g_adaptive = cv2.adaptiveThreshold(g_channel, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 11, 2)
r_adaptive = cv2.adaptiveThreshold(r_channel, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 11, 2)

# Combina os canais limiarizados
adaptive_color_image = cv2.merge((b_adaptive, g_adaptive, r_adaptive))

# Exibe a imagem original e a imagem limiarizada
cv2.imshow('Original Color Image', color_image)
cv2.imshow('Adaptive Threshold on Color Image', adaptive_color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
