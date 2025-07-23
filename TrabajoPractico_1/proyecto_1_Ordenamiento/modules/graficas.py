import sys
import os
import time
import matplotlib.pyplot as plt
import random 
from random import randint

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from modules.Radixsort import radix_sort
from modules.Ordenamiento_burbuja import ord_burbuja
from modules.Quicksort import ord_quicksort
from tests.tests import SortingTest

# Crear instancia y ejecutar test
tester = SortingTest()
tiempo_burbuja, tiempo_quicksort, tiempo_radixsort, tiempos_ordenados = tester.test_algoritmos()

# Crear la lista de tamaños para el eje X
tam_listas = list(range(1, 1001, 100))

# Graficar los resultados
plt.plot(tam_listas, tiempo_burbuja, label='Ord burbuja', marker='o')
plt.plot(tam_listas, tiempo_quicksort, label='Quick sort', marker='o')
plt.plot(tam_listas, tiempo_radixsort, label='Radix sort', marker='o')
plt.plot(tam_listas, tiempos_ordenados, label='Sorted (builtin)', marker='o')
plt.xlabel('Cantidad de elementos N')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de distintos algoritmos de ordenamiento')
plt.legend()
plt.grid(True)
plt.show()

"""Observaciones de la gráfica:
Ordenamiento Burbuja: Muestra un crecimiento exponencial(O(n 2))
Quicksort: O(NlogN) en el caso promedio.
Radix Sort: O(d⋅N) (donde d es el número de dígitoa)
sorted() (Timsort): También tiene una complejidad O(NlogN) """