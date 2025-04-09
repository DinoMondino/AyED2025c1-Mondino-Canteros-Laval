import sys
import os
import time
import matplotlib.pyplot as plt
import random 
from random import randint

# Ajuste para importar correctamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Importar las funciones de ordenamiento
from proyecto_1_Ordenamiento.modules.modulo1 import ord_burbuja, ord_quicksort, radix_sort
from proyecto_1_Ordenamiento.tests.test_modulo1 import SortingTest

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
