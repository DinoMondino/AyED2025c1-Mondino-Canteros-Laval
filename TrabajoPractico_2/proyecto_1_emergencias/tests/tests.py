# -*- coding: utf-8 -*-
from modules.modules import MonticuloBinario
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

    lista.insertar(paciente1)
    lista.insertar(paciente2)
    lista.insertar(paciente3)
    lista.insertar(paciente4)

    #lista.eliminarMin()
    print(lista.buscarMin())
    lista.eliminarMin()
    print(lista.buscarMin())
    lista.eliminarMin()
    print(lista.buscarMin())
    #print(lista.tamanio())