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


imagen = cv2.imread('elon.png', cv2.IMREAD_GRAYSCALE)

# Aplicar el filtro Sobel en x y en y con conversión de escala a 8 bits
sobel_x = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)

# Convertir a escala absoluta para obtener valores entre 0 y 255
sobel_x_abs = cv2.convertScaleAbs(sobel_x)
sobel_y_abs = cv2.convertScaleAbs(sobel_y)

# Calcular la magnitud de los gradientes con los valores absolutos
magnitud_sobel = np.sqrt(sobel_x**2 + sobel_y**2)

# Normalizar la magnitud a valores entre 0 y 255
magnitud_sobel_normalizada = cv2.normalize(magnitud_sobel, None, 0, 255, cv2.NORM_MINMAX)
magnitud_sobel_abs = cv2.convertScaleAbs(magnitud_sobel_normalizada)


cv2.imshow('Imagen Original', imagen)
cv2.imshow('Gradiente Sobel en X', sobel_x_abs)
cv2.imshow('Gradiente Sobel en Y', sobel_y_abs)
cv2.imshow('Magnitud de Gradientes Sobel', magnitud_sobel_abs)


cv2.waitKey(0)
cv2.destroyAllWindows()
