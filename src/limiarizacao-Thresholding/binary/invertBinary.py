import cv2

# Carrega a imagem em escala de cinza
# gray_image = cv2.imread('./assets/other/nanachi.bmp', cv2.IMREAD_GRAYSCALE)
gray_image = cv2.imread('./assets/other/nanachi.bmp')

# Aplicar a limiarização binária

threshold_value = 127  # O valor de limiar
max_value = 255  # O valor máximo após o limiar
_, binary_inv_thresh = cv2.threshold(gray_image, threshold_value, max_value, cv2.THRESH_BINARY_INV)

# Exibe o resultado
cv2.imshow('Invert binary Threshold', binary_inv_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()





