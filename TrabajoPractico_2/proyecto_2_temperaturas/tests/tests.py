import unittest
from modules.TemperaturasDB import Temperaturas_DB

class TestTemperaturasDB(unittest.TestCase):
    def setUp(self):
        self.db=Temperaturas_DB()
        self.db.guardar_temperatura(22.8,"02-12-2023")
        self.db.guardar_temperatura(23.2,"03-12-2023")
        self.db.guardar_temperatura(22.2,"04-12-2023")
        self.db.guardar_temperatura(25.0,"05-12-2023")

    def test_cantidad_muestras(self):
        self.assertEqual(self.db.cantidad_muestras(),4)

    def test_devolver_temperatura_existente(self):
        self.assertEqual(self.db.devolver_temperatura("04-12-2023"),22.2)

    def test_devolver_temperatura_inexistente(self):
        self.assertIsNone(self.db.devolver_temperatura("01-12-2023"))

    def test_listar_temperaturas_en_rango(self):
        resultados=self.db.listar_temperaturas_en_rango("02-12-2023","04-12-2023")
        self.assertEqual(len(resultados),3)

    def test_max_temp_rango(self):
        self.assertEqual(self.db.max_temp_rango("02-12-2023","05-12-2023"),25.0)

    def test_min_temp_rango(self):
        self.assertEqual(self.db.min_temp_rango("02-12-2023","05-12-2023"),22.2)

    def test_temp_extremos_rango(self):
        self.assertEqual(self.db.temp_extremos_rango("02-12-2023","05-12-2023"),(22.2,25.0))
    
    def test_borrar_temperatura(self):
        self.assertTrue(self.db.borrar_temperatura("03-12-2023"))
        self.assertEqual(self.db.cantidad_muestras(),3)
        self.assertIsNone(self.db.devolver_temperatura("03-12-2023"))

    def test_formato_incorrecto_fecha(self):
        with self.assertRaises(ValueError):
            self.db.guardar_temperatura(24.5,"16/01/2024")

    def test_devolver_temperaturas_formateadas(self):
        expectativa=[
            "02/12/2023: 22.8 °C"
            "03/12/2023: 23.2 °C"
            "04/12/2023: 22.2 °C"
        ]
        resultado=self.db.devolver_temperaturas("02-12-2023","04-12-2023")
        self.assertEqual(resultado,expectativa)
        
if __name__ =="__main__":
    unittest.main()