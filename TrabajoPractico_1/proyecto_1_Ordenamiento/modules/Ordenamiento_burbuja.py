
#Función ordenamiento burbuja
def ord_burbuja (lista_ordenar):    #define la función y toma como argumento una lista
    tamaño = len(lista_ordenar)     #calcula la longitud de la lista ingresada
    for i in range(tamaño):         #itera sobre cada elemento de la lista
        for j in range (0,tamaño-i-1):   #itera sobre los elementos restantes de la lista que aún no están ordenados
            if lista_ordenar [j]>lista_ordenar[j+1]:    #compara el elemento actual con el siguiente
                lista_ordenar[j],lista_ordenar[j+1]=lista_ordenar[j+1],lista_ordenar[j]  #si el elemento actual es mayor que el siguiente los intercambia
    return lista_ordenar           