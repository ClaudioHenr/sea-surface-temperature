import cv2

# Carrega a imagem em escala de cinza
# gray_image = cv2.imread('./assets/other/nanachi.bmp', cv2.IMREAD_GRAYSCALE)
gray_image = cv2.imread('./assets/other/nanachi.bmp')

# Aplicar
# O primeiro valor é o limiar, o segundo valor é o valor máximo
# O terceiro parâmetro é o tipo de limiarização, aqui estamos usando THRESH_BINARY
threshold_value = 127  # O valor de limiar
max_value = 255  # O valor máximo após o limiar
_, binary_thresh = cv2.threshold(gray_image, threshold_value, max_value, cv2.THRESH_BINARY)

# Exibe o resultado
cv2.imshow('Binary Threshold', binary_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()





