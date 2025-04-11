import unittest
from calculo_descuento_refactorizado import calcular_precio_final

class TestCalculoDescuento(unittest.TestCase):
    
    def test_descuento_20_por_ciento(self):
        resultado = calcular_precio_final(100, 20)
        self.assertEqual(resultado, 80)

    def test_descuento_0_por_ciento(self):
        resultado = calcular_precio_final(50, 0)
        self.assertEqual(resultado, 50)

    def test_descuento_100_por_ciento(self):
        resultado = calcular_precio_final(80, 100)
        self.assertEqual(resultado, 0)

if __name__ == '__main__':
    unittest.main()
