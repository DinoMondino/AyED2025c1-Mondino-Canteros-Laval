# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código.

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

#ordenamiento radix sort
def counting_sort(lista,digito_actual):
    n=len(lista)
    output=[0]*n     #la lista output de tamaño n para almacenar los elementos ordenados
    count=[0]*10     #la lista count de tamaño 10 (para los digitos del 0 al 9) se usará para contar la ocurrencia de cada dígito en la posición actual

    for i in range(n):  #el bucle itera con cada elemento de la lista ingresada 
        index=lista[i]//digito_actual #se calcula el indice de cada elemento lista[i] correspondiente en la lista count, nos da el digito en la posición actual que se considera 
        count[index % 10]+=1 #cuenta cuántas veces aparece cada dígito en la posición actual
    
    for i in range(1,10):
        count[i]+=count[i-1]#se utiliza para acumular conteos en la lista count, convierte a la lista count en una lista de posiciones donde cada posición indica la ubicación final de cada dígito de la lista ordenada
    
    for i in range(n-1,-1,-1): #se inicia el bucle que itera sobre la lista en orden inverso, para mantener la estabilidad del algoritmo
        index=lista[i]//digito_actual #se calcula el índice del elemento acutal
        output[count[index%10]-1]=lista[i] #se coloca el elemento en la posición correcta de output
        count[index%10]-=1 #se decrementa el conteo en count para el dígito actual

    for i in range(n):
        lista[i]=output[i] #se copia cada elemento de la lista output de vuelta a la lista original de modo que la lista contenga los elementos ordenados

def radix_sort(lista):
    maximo=max(lista) #se almacena el valor máximo de la lista a ordenar , para determinar luego cuántos dígitos tiene el número más grande ya que el algoritmo los va a ordenar dígito por dígito
    x=1 #se utiliza para representar la posición del dígito que estamos considerando(1=unidades, 10=decenas, etc)
    while maximo//x>0: 
        counting_sort(lista,x) #ordena la lista según el dígito de la posición actual
        x*=10    #se multiplica x para pasar al siguiente dígito
    return lista #devuelve la lista ya ordenada
        
