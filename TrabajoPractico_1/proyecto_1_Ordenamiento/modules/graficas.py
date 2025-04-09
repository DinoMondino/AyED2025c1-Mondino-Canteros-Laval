import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
# Para arreglar import from modulo1
from proyecto_1_Ordenamiento.tests.test_modulo1 import SortingTest
import time
import matplotlib.pyplot as plt
from random import randint




# Graficar los resultados
plt.plot(tam_listas, tiempo_burbuja, label='Ord burbuja', marker='o')
plt.plot(tam_listas, tiempo_quicksort, label='Quick sort', marker='o')
plt.plot(tam_listas, tiempo_radixsort, label='Radix sort', marker='o')
plt.plot(tam_listas, tiempos_ordenados, label='Radix sort', marker='o')
plt.xlabel('Cantidad de elementos N')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de métodos len, copiar, invertir')
plt.legend()
plt.grid(True)
plt.show()