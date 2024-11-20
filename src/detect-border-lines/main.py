import cv2
import numpy as np

# Carregar a imagem
image = cv2.imread('./assets/other/detect-line/copo.bmp')

# Converter a imagem para escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar suavização para reduzir ruídos
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Detectar bordas usando o detector de Canny
edges = cv2.Canny(blur, 50, 150)

# Detectar linhas usando a Transformada de Hough
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=50, maxLineGap=10)

# Desenhar as linhas detectadas na imagem original
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Exibir a imagem com as linhas detectadas
cv2.imshow('Linhas Detectadas', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
