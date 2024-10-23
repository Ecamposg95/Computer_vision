# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:19:29 2024

@author: ECG

I. Utilizando el ambiente de su elección (OpenCV, Octave, Matlab):

Abra una imagen (en escala de grises)
Aplique un filtro para calcular el gradiente en x: Gx = [0 0 0; -1 0 1; 0 0 0] / 2;
Aplique un filtro para calcular el gradiente en x: Gy = [0 -1 0; 0 0 0; 0 1 0] / 2;
Calcule la magnitud de los gradientes
Muestre la imagen original, la del gradiente en x, del gradiente en y, y de la magnitud de los gradientes.
 

II. Utilizando el ambiente de su elección (OpenCV, Octave, Matlab):

Realice los mismo pasos del ejercicio anterior, con el filtro de Sobel

"""

import cv2
import numpy as np


imagen = cv2.imread('pulp.jpg', cv2.IMREAD_GRAYSCALE)

# Definir los filtros Gx y Gy
Gx = np.array([[0, 0, 0], [-1, 0, 1], [0, 0, 0]], dtype=np.float32) / 2
Gy = np.array([[0, -1, 0], [0, 0, 0], [0, 1, 0]], dtype=np.float32) / 2

# Aplicar los filtros utilizando filter2D
gradiente_x = cv2.filter2D(imagen, -1, Gx)
gradiente_y = cv2.filter2D(imagen, -1, Gy)

# Calcular la magnitud de los gradientes
magnitud = np.sqrt(gradiente_x**2 + gradiente_y**2)
magnitud = np.uint8(magnitud)

# Mostrar las imágenes en ventanas separadas
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Gradiente en X', gradiente_x)
cv2.imshow('Gradiente en Y', gradiente_y)
cv2.imshow('Magnitud de Gradientes', magnitud)


cv2.waitKey(0)
cv2.destroyAllWindows()
