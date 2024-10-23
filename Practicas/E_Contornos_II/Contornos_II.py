# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:19:29 2024

@author: ECG

I. Utilizando el ambiente de su elección (OpenCV, Octave, Matlab):

Abra una imagen (a color)
Aplique un filtro para calcular el gradiente en x: Gx = [0 0 0; -1 0 1; 0 0 0] / 2;
Aplique un filtro para calcular el gradiente en x: Gy = [0 -1 0; 0 0 0; 0 1 0] / 2;
Calcule la magnitud de los gradientes
Muestre la imagen original, la del gradiente en x, del gradiente en y, y de la magnitud de los gradientes.
 

II. Utilizando el ambiente de su elección (OpenCV, Octave, Matlab):

Realice los mismo pasos del ejercicio anterior, con el filtro de Sobel
"""

import cv2
import numpy as np

# Abrir la imagen a color
imagen_color = cv2.imread('pulp.jpg')


canales = cv2.split(imagen_color)

# Definir los filtros Gx y Gy
Gx = np.array([[0, 0, 0], [-1, 0, 1], [0, 0, 0]], dtype=np.float32) / 2
Gy = np.array([[0, -1, 0], [0, 0, 0], [0, 1, 0]], dtype=np.float32) / 2

# Aplicar los filtros a cada canal
gradiente_x = [cv2.filter2D(canal, -1, Gx) for canal in canales]
gradiente_y = [cv2.filter2D(canal, -1, Gy) for canal in canales]

# Calcular la magnitud de los gradientes para cada canal y combinar
magnitud_canales = [np.sqrt(gx**2 + gy**2) for gx, gy in zip(gradiente_x, gradiente_y)]
magnitud_canales = [np.uint8(magnitud) for magnitud in magnitud_canales]


gradiente_x_color = cv2.merge(gradiente_x)
gradiente_y_color = cv2.merge(gradiente_y)
magnitud_color = cv2.merge(magnitud_canales)


cv2.imshow('Imagen Original', imagen_color)
cv2.imshow('Gradiente en X (Color)', gradiente_x_color)
cv2.imshow('Gradiente en Y (Color)', gradiente_y_color)
cv2.imshow('Magnitud de Gradientes (Color)', magnitud_color)


cv2.waitKey(0)
cv2.destroyAllWindows()
