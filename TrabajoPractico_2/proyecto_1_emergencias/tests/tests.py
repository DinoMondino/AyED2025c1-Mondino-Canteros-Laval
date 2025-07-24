# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from modules.monticulo import MonticuloBinario
from modules.modules import Paciente
"""mini testeo de funciones"""
lista = MonticuloBinario()
paciente1 = Paciente()
print(paciente1.get_riesgo())
paciente2 = Paciente()
print(paciente2.get_riesgo())
paciente3 = Paciente()
print(paciente3.get_riesgo())
paciente4 = Paciente()
print(paciente4.get_riesgo())

lista._insertar(paciente1)
lista._insertar(paciente2)
lista._insertar(paciente3)
lista._insertar(paciente4)

#lista.eliminarMin()
print(lista._buscarMin())
lista._eliminarMin()
print(lista._buscarMin())
lista._eliminarMin()
print(lista._buscarMin())
#print(lista.tamanio())