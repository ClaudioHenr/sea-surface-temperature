import cv2

# Carrega a imagem em escala de cinza
gray_image = cv2.imread('./assets/other/nanachi.bmp', cv2.IMREAD_GRAYSCALE)
# gray_image = cv2.imread('./assets/other/nanachi.bmp')

# Aplica a limiarização de Otsu
_, otsu_threshold = cv2.threshold(gray_image, 0, 255, cv2.THRESH_OTSU)
# _, otsu_threshold = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Exibe o resultado
cv2.imshow('Otsu Threshold', otsu_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
