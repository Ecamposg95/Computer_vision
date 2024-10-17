# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:47:03 2024

@author: ECG
Emmanuel Campos Genaro
"""

import numpy as np
import pandas as pd

# Definición de los conjuntos de valores
A = np.array([-1, 1, 2, 1, -1])
B = np.array([-1, 1, 2, 1, -1])
C = np.array([1, 2, 2, 3, 1])
D = np.array([0, -1, -2, 1, -1])
E = np.array([10, 11, 22, 11, 11])

# Cálculo de la correlación
correlations = {
    "A vs B": np.corrcoef(A, B)[0, 1],
    "A vs C": np.corrcoef(A, C)[0, 1],
    "A vs D": np.corrcoef(A, D)[0, 1],
    "A vs E": np.corrcoef(A, E)[0, 1],
    "B vs C": np.corrcoef(B, C)[0, 1],
    "B vs D": np.corrcoef(B, D)[0, 1],
    "B vs E": np.corrcoef(B, E)[0, 1],
    "C vs D": np.corrcoef(C, D)[0, 1],
    "C vs E": np.corrcoef(C, E)[0, 1],
    "D vs E": np.corrcoef(D, E)[0, 1]
}

# Mostramos los resultados en un DataFrame
df_correlations = pd.DataFrame(list(correlations.items()), columns=["Comparación", "Correlación"])
print(df_correlations)
