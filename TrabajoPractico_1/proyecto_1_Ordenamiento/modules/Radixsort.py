# RADIX SORT
# Ordena los números dígito por dígito, desde el dígito menos significativo hasta el más significativo.
# Para cada posición de dígito, utiliza Counting Sort para colocar los elementos en su posición.
# Este proceso se repite para cada dígito hasta que todos los números están ordenados.

def counting_sort(lista,digito_actual):
    n=len(lista)
    output=[0]*n    
    # lista  para almacenar los elementos ordenados
    count=[0]*10
    # lista para digitos del 0 al 9, para contar la ocurrencia de cada dígito en la posición actual

    for i in range(n):  # itera con cada elemento de la lista ingresada 
        index=lista[i]//digito_actual
        # calcula el indice de cada elemento lista[i] en la posición actual
        count[index % 10]+=1 
        # incrementa el contador para el dígito en count
    for i in range(1,10):
        count[i]+=count[i-1]
        # la convierte en una lista que indica la ubicación final de cada dígito en la lista ordenada.
    
    for i in range(n-1,-1,-1): # itera sobre la lista en orden inverso, para mantener la estabilidad del algoritmo
        index=lista[i]//digito_actual 
        # se calcula el índice del elemento acutal
        output[count[index%10]-1]=lista[i] 
        # se coloca el elemento en la posición correcta de output
        count[index%10]-=1 # se decrementa el conteo en count para el dígito actual

    for i in range(n):
        lista[i]=output[i] 
        # se copian los elemento del output a la lista original de modo que la lista contenga los elementos ordenados

def radix_sort(lista):
    maximo=max(lista) 
    # para determinar cuántos dígitos tiene el número más grande
    x=1 
    # se utiliza para representar la posición del dígito que estamos considerando(1=unidades, 10=decenas, etc)
    while maximo//x>0: 
        counting_sort(lista,x) # ordena la lista según el dígito de la posición actual
        x*=10    # se multiplica x para pasar al siguiente dígito
    return lista # devuelve la lista ya ordenada
