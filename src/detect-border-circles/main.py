import cv2
import numpy as np

# Carregar a imagem
img = cv2.imread('./assets/other/detect-line/copo.bmp', cv2.IMREAD_GRAYSCALE)

# Aplicar suavização para reduzir ruídos
# blur = cv2.GaussianBlur(img, (5, 5), 0)
blur = cv2.medianBlur(img, 5)

# Detectar círculos usando a Transformada de Hough para Círculos
circles = cv2.HoughCircles(blur, 
                           cv2.HOUGH_GRADIENT, 
                           dp=1.2, 
                           minDist=30, 
                           param1=50, 
                           param2=30, 
                           minRadius=10, 
                           maxRadius=100)

# Garantir que círculos foram detectados
if circles is not None:
    circles = np.uint16(np.around(circles))  # Arredondar valores
    for circle in circles[0, :]:
        # Extrair coordenadas do centro e raio
        x, y, r = circle
        # Desenhar o contorno do círculo
        cv2.circle(img, (x, y), r, (0, 255, 0), 2)
        # Desenhar o centro do círculo
        cv2.circle(img, (x, y), 2, (0, 0, 255), 3)

# Mostrar a imagem com as linhas detectadas
cv2.imshow('Imagem com Circulos', img)
cv2.waitKey(0)
cv2.destroyAllWindows()