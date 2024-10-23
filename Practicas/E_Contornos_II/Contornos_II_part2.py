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

# Separar los canales de color
canales = cv2.split(imagen_color)

# Aplicar el filtro Sobel en x y en y para cada canal
sobel_x = [cv2.Sobel(canal, cv2.CV_64F, 1, 0, ksize=3) for canal in canales]
sobel_y = [cv2.Sobel(canal, cv2.CV_64F, 0, 1, ksize=3) for canal in canales]

# Convertir a escala absoluta para cada canal
sobel_x_abs = [cv2.convertScaleAbs(gx) for gx in sobel_x]
sobel_y_abs = [cv2.convertScaleAbs(gy) for gy in sobel_y]

# Calcular la magnitud de los gradientes para cada canal
magnitud_canales = [np.sqrt(gx**2 + gy**2) for gx, gy in zip(sobel_x, sobel_y)]
magnitud_canales = [cv2.convertScaleAbs(magnitud) for magnitud in magnitud_canales]

# Combinar los canales para formar las imágenes finales
sobel_x_color = cv2.merge(sobel_x_abs)
sobel_y_color = cv2.merge(sobel_y_abs)
magnitud_color = cv2.merge(magnitud_canales)


cv2.imshow('Imagen Original', imagen_color)
cv2.imshow('Gradiente Sobel en X (Color)', sobel_x_color)
cv2.imshow('Gradiente Sobel en Y (Color)', sobel_y_color)
cv2.imshow('Magnitud de Gradientes Sobel (Color)', magnitud_color)


cv2.waitKey(0)
cv2.destroyAllWindows()
