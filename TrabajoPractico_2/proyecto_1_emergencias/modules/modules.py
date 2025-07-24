from random import randint, choices
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from .monticulo import MonticuloBinario, ColadePrioridad
import itertools # Importamos itertools para generar IDs únicos

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo'] # probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6]

# Generador de IDs únicos para el orden de llegada
next_id = itertools.count()

class Paciente:
    def __init__(self):
        self.nombre = nombres[randint(0, len(nombres) - 1)]
        self.apellido = apellidos[randint(0, len(apellidos) - 1)]
        self.riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.descripcion = descripciones_de_riesgo[self.riesgo - 1]
        self.orden_llegada = next(next_id) # Asignamos un ID único al paciente

    def __str__(self):
        return f"{self.nombre} {self.apellido} -> Riesgo: {self.riesgo}-{self.descripcion}, Orden de Llegada: {self.orden_llegada}"

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_riesgo(self):
        return self.riesgo

    def get_descripcion_riesgo(self):
        return self.descripcion

    # Implementamos métodos de comparación para que el montículo pueda comparar pacientes.
    def __lt__(self, other):
        if self.riesgo < other.riesgo: # Primero por riesgo
            return True
        elif self.riesgo == other.riesgo: # Si los riesgos =, compara por orden de llegada 
            return self.orden_llegada < other.orden_llegada
        return False

    def __gt__(self, other):
        # Inverso de __lt__
        if self.riesgo > other.riesgo:
            return True
        elif self.riesgo == other.riesgo:
            return self.orden_llegada > other.orden_llegada
        return False

    def __eq__(self, other):
        return self.riesgo == other.riesgo and self.orden_llegada == other.orden_llegada

"""
# Ejemplo de uso
if __name__ == "__main__":
    print("--- Ejemplo de uso de Cola de Prioridad ---")
    cola = ColadePrioridad()
    for _ in range(10):
        paciente = Paciente()
        cola.insertar(paciente)
        print(f"Insertando: {paciente}")

    print("\n--- Pacientes atendidos por orden de prioridad ---")
    while not cola.lista._estaVacio(): 
        print(cola.eliminarMax())
"""