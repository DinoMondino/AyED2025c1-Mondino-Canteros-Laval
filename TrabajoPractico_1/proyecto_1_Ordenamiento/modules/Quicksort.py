                                         
#Función quicksort 
def ord_quicksort(lista_ordenar):  #define la función y toma como argumento una lista
    if len(lista_ordenar)<=1:      #si la lista tiene uno o cero elementos, ya está ordenada, se devuelve como ingresó
        return lista_ordenar       
    pivot=lista_ordenar[len(lista_ordenar)//2]    #selecciona un elemento como pivote, en este caso selecciona el del medio
    izquierda=[i for i in lista_ordenar if i<pivot]     #crea una lista con los elementos de la lista original menores al pivote
    medio=[i for i in lista_ordenar if i==pivot]        #crea una lista con los elementos de la lista original iguales al pivote
    derecha=[i for i in lista_ordenar if i>pivot]       #crea una lista con los elementos de la lista original mayores al pivote
    return ord_quicksort(izquierda)+medio+ord_quicksort(derecha)  #llama recursivamente a la función en las listas "izquierda" y "derecha" y concatena los resultados