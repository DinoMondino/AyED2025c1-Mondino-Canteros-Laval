import heapq
import os
from collections import defaultdict

# Leer el archivo y construir el grafo
def construir_grafo(filename):
    grafo = defaultdict(list)
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():  # Ignorar líneas vacías
                partes = line.strip().split(', ')
            if len(partes) != 3:
                print(f"[Línea inválida] '{line.strip()}' — Se esperaba 'origen, destino, distancia'")
                continue
            s, t, d = partes
            try:
                d = int(d)
            except ValueError:
                print(f"[Error] Distancia no válida en línea: '{line.strip()}'")
                continue
            grafo[s].append((t, d))
            grafo[t].append((s, d))  # Asumimos que las distancias son bidireccionales

        return grafo

#  Dijkstra
def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    padres = {nodo: None for nodo in grafo}
    cola_prioridad = [(0, inicio)]  # (distancia, nodo)

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if distancia_actual > distancias[nodo_actual]:
            continue

        for vecino, peso in grafo[nodo_actual]:
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                padres[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))

    return distancias, padres

# Función principal
def main():
    ruta = "data/aldeas.txt"
    if not os.path.exists(ruta):
        print(f"Error: el archivo no existe en la ruta {ruta}")
        return
    
    grafo = construir_grafo(ruta)
    inicio = 'Peligros'
    distancias, padres = dijkstra(grafo, inicio)
    

    # Mostrar la lista de aldeas en orden alfabético
    aldeas = sorted(grafo.keys())
    print("Aldeas en orden alfabético:")
    for aldea in aldeas:
        print(aldea)

    # Mostrar de qué vecina debería recibir la noticia y a qué vecinas debería enviar réplicas
    print("\nDistribución de mensajes:")
    for aldea in aldeas:
        if aldea == inicio:
            continue
        print(f"{aldea}: Recibe de {padres[aldea]}, Envía a ", end="")
        vecinos = [vecino for vecino, _ in grafo[aldea] if vecino != padres[aldea]]
        print(", ".join(vecinos) if vecinos else "Nadie")

    # Calcular la suma total de distancias recorridas
    total_distancia = sum(distancias[aldea] for aldea in aldeas if aldea != inicio)
    print(f"\nSuma total de distancias recorridas: {total_distancia}")

if __name__ == "__main__":
    main()

## Para el informe: 
#Construcción del grafo: Leemos el archivo y construimos un grafo utilizando un diccionario donde cada aldea tiene una lista de tuplas que representan sus aldeas vecinas y las distancias a ellas.

#Algoritmo de Dijkstra: Implementamos el algoritmo para encontrar las distancias más cortas desde "Peligros" a todas las demás aldeas, así como los nodos padres que indican de dónde se recibe el mensaje.

#Mostrar resultados: Imprimimos la lista de aldeas, de qué aldea reciben el mensaje y a qué aldeas envían réplicas, así como la suma total de distancias recorridas.
