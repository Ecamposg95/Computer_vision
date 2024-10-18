
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 22:59:52 2024

@author: ecamp
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


imagen_bn = cv2.imread('reloj.png', cv2.IMREAD_GRAYSCALE)

if imagen_bn is None:
    print("Error: No se puede cargar la imagen 'reloj.png'. Verifica la ruta.")
    exit()

# Definir la Región de Interés (ROI)
x, y, w, h = 70, 70, 120, 120  # Coordenadas de la ROI (x, y, ancho, alto)
roi_bn = imagen_bn[y:y+h, x:x+w]

# Correlacionar la ROI con la imagen original
resultado_correlacion_bn = cv2.matchTemplate(imagen_bn, roi_bn, method=cv2.TM_CCOEFF_NORMED)

# Graficar la correlación como imagen
plt.figure(figsize=(10, 5))
plt.imshow(resultado_correlacion_bn, cmap='gray')
plt.title("Correlación (Escala de Grises)")
plt.colorbar()
plt.show()

# Graficar la correlación como superficie
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(range(resultado_correlacion_bn.shape[1]), range(resultado_correlacion_bn.shape[0]))
ax.plot_surface(X, Y, resultado_correlacion_bn, cmap='viridis')
plt.title("Superficie de Correlación (Escala de Grises)")
plt.show()

# Encontrar el punto de mayor correlación
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado_correlacion_bn)

# Dibujar un recuadro donde se encontró la mayor correlación
top_left_bn = max_loc
bottom_right_bn = (top_left_bn[0] + w, top_left_bn[1] + h)
imagen_bn_rect = imagen_bn.copy()
cv2.rectangle(imagen_bn_rect, top_left_bn, bottom_right_bn, 255, 2)

# Mostrar la imagen original con la ROI señalada
cv2.imshow("Imagen original con ROI detectada (Escala de grises)", imagen_bn_rect)


cv2.waitKey(0)
cv2.destroyAllWindows()
