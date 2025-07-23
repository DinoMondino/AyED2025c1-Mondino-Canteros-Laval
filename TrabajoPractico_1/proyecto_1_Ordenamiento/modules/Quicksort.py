# Función QUIKCSORT: "divide y vencerás".
# Funciona seleccionando 'pivote' de la lista y particionando los otros elementos
# en dos sub-listas: una para elementos menores que el pivote y otra para elementos mayores.
# Luego, el algoritmo se aplica recursivamente a las dos sub-listas.

def ord_quicksort(lista_ordenar): 
    if len(lista_ordenar)<=1:
    #si la lista tiene uno o cero elementos, ya está ordenada
        return lista_ordenar       
    pivot=lista_ordenar[len(lista_ordenar)//2]    # selecciona como pivote  el del medio
    izquierda=[i for i in lista_ordenar if i<pivot]     
    # crea una lista con los elementos de la lista original menores al pivote
    medio=[i for i in lista_ordenar if i==pivot]        
    # crea una lista con los elementos de la lista original iguales al pivote
    derecha=[i for i in lista_ordenar if i>pivot]
    # crea una lista con los elementos de la lista original mayores al pivote
    return ord_quicksort(izquierda)+medio+ord_quicksort(derecha)  
    # llama recursivamente a la función en las listas "izquierda" y "derecha" y concatena los resultados