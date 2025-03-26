# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código.

import random
import math
#Función ordenamiento burbuja
def ord_burbuja (lista_ordenar):    #define la función y toma como argumento una lista
    tamaño = len(lista_ordenar)     #calcula la longitud de la lista ingresada
    for i in range(tamaño):         #itera sobre cada elemento de la lista
        for j in range (0,tamaño-i-1):   #itera sobre los elementos restantes de la lista que aún no están ordenados
            if lista_ordenar [j]>lista_ordenar[j+1]:    #compara el elemento actual con el siguiente
                lista_ordenar[j],lista_ordenar[j+1]=lista_ordenar[j+1],lista_ordenar[j]  #si el elemento actual es mayor que el siguiente los intercambia
    return lista_ordenar           
                                               
#Función quicksort 
def ord_quicksort(lista_ordenar):  #define la función y toma como argumento una lista
    if len(lista_ordenar)<=1:      #si la lista tiene uno o cero elementos, ya está ordenada, se devuelve como ingresó
        return lista_ordenar       
    pivot=lista_ordenar[len(lista_ordenar)//2]    #selecciona un elemento como pivote, en este caso selecciona el del medio
    izquierda=[i for i in lista_ordenar if i<pivot]     #crea una lista con los elementos de la lista original menores al pivote
    medio=[i for i in lista_ordenar if i==pivot]        #crea una lista con los elementos de la lista original iguales al pivote
    derecha=[i for i in lista_ordenar if i>pivot]       #crea una lista con los elementos de la lista original mayores al pivote
    return ord_quicksort(izquierda)+medio+ord_quicksort(derecha)  #llama recursivamente a la función en las listas "izquierda" y "derecha" y concatena los resultados