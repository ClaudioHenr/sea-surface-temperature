import cv2
import numpy as np

# Carregar a imagem
img = cv2.imread('./assets/other/detect-line/mesa-de-frutas.bmp', cv2.IMREAD_GRAYSCALE)

# Aplicar suavização para reduzir ruídos
blur = cv2.GaussianBlur(img, (5, 5), 0)

# Aplicar a detecção de bordas (opcional, para melhorar a detecção de linhas)
edges = cv2.Canny(blur, 50, 150)

# Aplicar a transformada de Hough para linhas
lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=10, minLineLength=50, maxLineGap=10)

# Desenhar as linhas na imagem
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Mostrar a imagem com as linhas detectadas
cv2.imshow('Imagem com Linhas', img)
cv2.waitKey(0)
cv2.destroyAllWindows()