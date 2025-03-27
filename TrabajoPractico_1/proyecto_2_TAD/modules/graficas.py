from TrabajoPractico_1/proyecto_2_TAD/modules/modulo1.py import Nodo, ListaDobleEnlazada
import matplotlib.pyplot as plt
from random import randint

import time

lista = ListaDobleEnlazada()

def medir_tiempo(funcion, lista):
    inicio = time.time()
    funcion(lista)
    fin = time.time()
    return fin - inicio

tam_listas = [10, 100, 500, 1000, 5000, 10000]
tiempos_len = []
tiempos_copiar = []
tiempos_invertir = []

for tam in tam_listas:
    lista = ListaDobleEnlazada()
    
    # Agregar elementos a la lista
    for i in range(tam):
        lista.agregar_al_final(i)
    
    # Medir tiempo de len
    tiempos_len.append(medir_tiempo(lambda x: len(x), lista))
    
    # Medir tiempo de copiar
    tiempos_copiar.append(medir_tiempo(lambda x: x.copiar(), lista))
    
    # Medir tiempo de invertir
    tiempos_invertir.append(medir_tiempo(lambda x: x.invertir(), lista))

# Graficar los resultados
plt.plot(tam_listas, tiempos_len, label='len', marker='o')
plt.plot(tam_listas, tiempos_copiar, label='copiar', marker='o')
plt.plot(tam_listas, tiempos_invertir, label='invertir', marker='o')
plt.xlabel('Cantidad de elementos N')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de métodos len, copiar, invertir')
plt.legend()
plt.grid(True)
plt.show()
