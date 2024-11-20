import cv2

# Carrega a imagem colorida
color_image = cv2.imread('./assets/other/nanachi.bmp')

# Verifica se a imagem foi carregada corretamente
if color_image is None:
    raise ValueError("Imagem não encontrada. Verifique o caminho do arquivo.")

# Converte para tons de cinza
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# Aplica a limiarização adaptativa
adaptive_threshold = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                           cv2.THRESH_BINARY, 11, 2)

# Exibe a imagem original e a imagem limiarizada
cv2.imshow('Original Color Image', color_image)
cv2.imshow('Adaptive Threshold on Grayscale Image', adaptive_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
