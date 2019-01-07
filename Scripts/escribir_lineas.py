# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 22:37:35 2019

@author: leobo
"""

import sys

if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    
    for r in range(repeticiones):
        print(texto)
else:
    print("Error, introduce los argumentos correctamente")
    print("Ejemplo: escribir_lineas.py 'Text' #")