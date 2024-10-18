# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 23:10:06 2024

@author: ecamp
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


imagen_color = cv2.imread('siqueiros.jpeg')

if imagen_color is None:
    print("Error: No se puede cargar la imagen 'siqueiros.jpeg'. Verifica la ruta.")
    exit()

# Definir la Región de Interés (ROI)
x, y, w, h = 50, 50, 100, 100  # Coordenadas de la ROI (x, y, ancho, alto)
roi_color = imagen_color[y:y+h, x:x+w]


resultado_correlacion_color = cv2.matchTemplate(imagen_color, roi_color, method=cv2.TM_CCOEFF_NORMED)

plt.figure(figsize=(10, 5))
plt.imshow(resultado_correlacion_color, cmap='hot')
plt.title("Correlación (Color)")
plt.colorbar()
plt.show()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(range(resultado_correlacion_color.shape[1]), range(resultado_correlacion_color.shape[0]))
ax.plot_surface(X, Y, resultado_correlacion_color, cmap='inferno')
plt.title("Superficie de Correlación (Color)")
plt.show()

# Encontrar el punto de mayor correlación
min_val_color, max_val_color, min_loc_color, max_loc_color = cv2.minMaxLoc(resultado_correlacion_color)


top_left_color = max_loc_color
bottom_right_color = (top_left_color[0] + w, top_left_color[1] + h)
imagen_color_rect = imagen_color.copy()
cv2.rectangle(imagen_color_rect, top_left_color, bottom_right_color, (0, 255, 0), 2)


cv2.imshow("Imagen original con ROI detectada (Color)", imagen_color_rect)


cv2.waitKey(0)
cv2.destroyAllWindows()