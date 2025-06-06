import os
from modules.Aldeas import construir_grafo, prim, procesar_red

def main():
    ruta = "docs/aldeas.txt"
    if not os.path.exists(ruta):
        print(f"Error: el archivo no existe en la ruta {ruta}")
        return

    grafo = construir_grafo(ruta)
    inicio = 'Peligros'
    mst = prim(grafo, inicio)

    recibe_de, envia_a = procesar_red(mst)

    # aldeas involucradas
    aldeas = set(grafo.keys())
    aldeas_ordenadas = sorted(aldeas)

    print("Estado de la red de mensajes:")
    for aldea in aldeas_ordenadas:
        # Peligros no recibe
        origen = recibe_de.get(aldea, None)
        # réplicas
        destinos = envia_a.get(aldea, [])

        if aldea == inicio:
            print(f"{aldea}: Origen (no recibe de nadie)")
        else:
            print(f"{aldea}: Recibe de {origen}")

        if destinos:
            print(f"  Envía réplica a: {', '.join(destinos)}")
        else:
            print(f"  No envía réplicas")

    # conexiones MST ordenadas
    print("\nConexiones para enviar el mensaje (MST):")
    for u, v, peso in sorted(mst):
        print(f"{u} > {v} ({peso} leguas)")

    # distancia 
    total = sum(peso for _, _, peso in mst)
    print(f"\nDistancia total mínima para entregar el mensaje: {total} leguas")

if __name__ == "__main__":
    main()
