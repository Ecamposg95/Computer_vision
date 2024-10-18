# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 22:44:09 2024

@author: ecamp
Emmanuel Campos Genaro
Script para procesar una imagen en escala de grises
"""

import cv2
import numpy as np

# Función para agregar ruido sal y pimienta
def agregar_ruido_sal_pimienta(imagen, porcentaje_ruido):
    salida = np.copy(imagen)
    cantidad = int(np.ceil(porcentaje_ruido * imagen.size))
    

    coords = [np.random.randint(0, i - 1, cantidad) for i in imagen.shape]
    salida[coords[0], coords[1]] = 255  # Sal
    coords = [np.random.randint(0, i - 1, cantidad) for i in imagen.shape]
    salida[coords[0], coords[1]] = 0  # Pimienta
    return salida

# Procesar imagen en escala de grises
def procesar_imagen_bn(ruta_imagen):
    # Cargar la imagen en escala de grises
    imagen_bn = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)

    if imagen_bn is None:
        print(f"No se pudo cargar la imagen: {ruta_imagen}. Verifica la ruta.")
        return

    # Agregar ruido sal y pimienta
    imagen_ruido_bn = agregar_ruido_sal_pimienta(imagen_bn, 0.05)

    # Aplicar filtro de media
    imagen_media_bn = cv2.blur(imagen_ruido_bn, (3, 3))

    # Aplicar filtro de mediana
    imagen_mediana_bn = cv2.medianBlur(imagen_ruido_bn, 3)


    cv2.imshow("Original en escala de grises", imagen_bn)
    cv2.imshow("Con ruido sal y pimienta (BN)", imagen_ruido_bn)
    cv2.imshow("Filtro de media (BN)", imagen_media_bn)
    cv2.imshow("Filtro de mediana (BN)", imagen_mediana_bn)


ruta_bn = 'reloj.png'
procesar_imagen_bn(ruta_bn)


cv2.waitKey(0)
cv2.destroyAllWindows()