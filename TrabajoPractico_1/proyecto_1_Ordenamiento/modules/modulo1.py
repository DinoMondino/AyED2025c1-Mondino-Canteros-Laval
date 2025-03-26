# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código.

import random
import math
def ord_burbuja (lista_ordenar):
    tamaño = len(lista_ordenar)
    for i in range(tamaño):
        for j in range (0,tamaño-i-1):
            if lista_ordenar [j]>lista_ordenar[j+1]:
                lista_ordenar[j],lista_ordenar[j+1]=lista_ordenar[j+1],lista_ordenar[j]
    return lista_ordenar           
                                               
            