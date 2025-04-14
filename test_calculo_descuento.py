# test_calculo_descuento.py

import unittest
from calculo_descuento_refactorizado import calcular_descuento_cliente

class TestCalculoDescuentoCliente(unittest.TestCase):
    
    def test_regular_mayor_a_1000(self):
        # Para "regular" con monto 1500, descuento debe ser: 1500 * 0.05 = 75
        self.assertEqual(calcular_descuento_cliente("regular", 1500), 75)
    
    def test_regular_menor_o_igual_a_1000(self):
        # Para "regular" con monto 1000, descuento debe ser: 1000 * 0.02 = 20
        self.assertEqual(calcular_descuento_cliente("regular", 1000), 20)
    
    def test_vip_mayor_a_1000(self):
        # Para "vip" con monto 1500, descuento: 1500 * 0.10 = 150
        self.assertEqual(calcular_descuento_cliente("vip", 1500), 150)
    
    def test_vip_menor_o_igual_a_1000(self):
        # Para "vip" con monto 1000, descuento: 1000 * 0.05 = 50
        self.assertEqual(calcular_descuento_cliente("vip", 1000), 50)
    
    def test_nuevo_mayor_a_1000(self):
        # Para "nuevo" con monto 1500, descuento: 1500 * 0.03 = 45
        self.assertEqual(calcular_descuento_cliente("nuevo", 1500), 45)
    
    def test_nuevo_menor_o_igual_a_1000(self):
        # Para "nuevo" con monto 1000, descuento: 1000 * 0.01 = 10
        self.assertEqual(calcular_descuento_cliente("nuevo", 1000), 10)
    
    def test_tipo_cliente_invalido(self):
        # Para un tipo de cliente no definido, se espera 0 de descuento.
        self.assertEqual(calcular_descuento_cliente("invalido", 1500), 0)

if __name__ == '__main__':
    unittest.main()
