# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 22:53:17 2024

@author: ecamp
Emmanuel Campos Genaro

Script para procesar una imagen a color

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


def procesar_imagen_color(ruta_imagen):

    imagen_color = cv2.imread(ruta_imagen)

    if imagen_color is None:
        print(f"No se pudo cargar la imagen: {ruta_imagen}. Verifica la ruta.")
        return

    # Agregar ruido sal y pimienta a cada canal de la imagen a color
    imagen_ruido_color = np.copy(imagen_color)
    for i in range(3): 
        imagen_ruido_color[:, :, i] = agregar_ruido_sal_pimienta(imagen_color[:, :, i], 0.05)

    # Aplicar filtro de media a la imagen a color
    imagen_media_color = cv2.blur(imagen_color, (3, 3))

    # Aplicar filtro de mediana a la imagen a color
    imagen_mediana_color = cv2.medianBlur(imagen_color, 3)


    cv2.imshow("Original a color", imagen_color)
    cv2.imshow("Con ruido sal y pimienta (Color)", imagen_ruido_color)
    cv2.imshow("Filtro de media (Color)", imagen_media_color)
    cv2.imshow("Filtro de mediana (Color)", imagen_mediana_color)


ruta_color = 'siqueiros.jpeg'
procesar_imagen_color(ruta_color)


cv2.waitKey(0)
cv2.destroyAllWindows()