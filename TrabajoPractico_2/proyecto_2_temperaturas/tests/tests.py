import unittest
from datetime import datetime

from proyecto_2_temperaturas.modules import modules

class TestTemperaturasDB(unittest.TestCase):
    def setUp(self):
        self.db=TestTemperaturasDB()
        self.db.guardar_temperatura(22.8,"02-12-2023")
        self.db.guardar_temperatura(23.2,"03-12-2023")
        self.db.guardar_temperatura(22.2,"04-12-2023")
        self.db.guardar_temperatura(25.0,"05-12-2023")

    def test_cantidad_muestras(self):
        self.assertEqual(self.db.cantidad_muestras(),4)

    def test_devolver_temperatura_existente(self):
        self.assertEqual(self.db.devolver_temperatura("04-12-2023"),22.2)
        