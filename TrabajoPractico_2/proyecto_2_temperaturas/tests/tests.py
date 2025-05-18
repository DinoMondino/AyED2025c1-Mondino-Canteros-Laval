import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from proyecto_2_temperaturas.modules.modules import Temperaturas_DB

class TestTemperaturasDB(unittest.TestCase):
    def setUp(self):
        self.db = Temperaturas_DB()

    def test_guardar_y_devolver_temperatura(self):
        self.db.guardar_temperatura(25.0, "2023-01-01")
        self.assertEqual(self.db.devolver_temperatura("2023-01-01"), 25.0)

    def test_devolver_temperatura_no_existente(self):
        self.assertIsNone(self.db.devolver_temperatura("2023-01-02"))

    def test_max_temp_rango(self):
        self.db.guardar_temperatura(20.0, "2023-01-01")
        self.db.guardar_temperatura(25.0, "2023-01-02")
        self.db.guardar_temperatura(30.0, "2023-01-03")
        self.assertEqual(self.db.max_temp_rango("2023-01-01", "2023-01-03"), 30.0)

    def test_min_temp_rango(self):
        self.db.guardar_temperatura(20.0, "2023-01-01")
        self.db.guardar_temperatura(25.0, "2023-01-02")
        self.db.guardar_temperatura(30.0, "2023-01-03")
        self.assertEqual(self.db.min_temp_rango("2023-01-01", "2023-01-03"), 20.0)

    def test_temp_extremos_rango(self):
        self.db.guardar_temperatura(20.0, "2023-01-01")
        self.db.guardar_temperatura(25.0, "2023-01-02")
        self.db.guardar_temperatura(30.0, "2023-01-03")
        min_temp, max_temp = self.db.temp_extremos_rango("2023-01-01", "2023-01-03")
        self.assertEqual(min_temp, 20.0)
        self.assertEqual(max_temp, 30.0)

    def test_borrar_temperatura(self):
        self.db.guardar_temperatura(25.0, "2023-01-01")
        self.db.borrar_temperatura("2023-01-01")
        self.assertIsNone(self.db.devolver_temperatura("2023-01-01"))

    def test_devolver_temperaturas(self):  
        self.db.guardar_temperatura(20.0, "2023-01-01")
        self.db.guardar_temperatura(25.0, "2023-01-02")
        self.db.guardar_temperatura(30.0, "2023-01-03")
        temperaturas = self.db.devolver_temperaturas("2023-01-01", "2023-01-03")
        self.assertEqual(len(temperaturas), 3)
        self.assertEqual(temperaturas[0], ("2023-01-01", 20.0))
        self.assertEqual(temperaturas[1], ("2023-01-02", 25.0))
        self.assertEqual(temperaturas[2], ("2023-01-03", 30.0))

    def test_cantidad_muestras(self):
        self.assertEqual(self.db.cantidad_muestras(), 0)
        self.db.guardar_temperatura(25.0, "2023-01-01")
        self.assertEqual(self.db.cantidad_muestras(), 1)

if __name__ == '__main__':
    unittest.main()
