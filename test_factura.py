"""
test_factura.py
---------------
Este archivo contiene pruebas unitarias para la función calcular_total_factura,
la cual calcula el total final de la factura a partir de una lista de productos,
el porcentaje de descuento, impuestos y costo de envío.
"""

import unittest
from factura_refactorizado import calcular_total_factura

class TestFacturaFinal(unittest.TestCase):
    
    def test_factura_sin_descuento(self):
        # Productos: [(nombre, cantidad, precio_unitario)]
        productos = [("Producto1", 2, 50), ("Producto2", 3, 30)]
        # Total = 2*50 + 3*30 = 100 + 90 = 190
        # Sin descuento, sin impuestos, sin envío.
        resultado = calcular_total_factura(productos, 0, 0, 0)
        self.assertEqual(resultado, 190)
    
    def test_factura_con_descuento(self):
        productos = [("Producto1", 4, 25)]
        # Total = 4*25 = 100
        # Descuento del 10%: 100 - 10 = 90
        resultado = calcular_total_factura(productos, 10, 0, 0)
        self.assertEqual(resultado, 90)
    
    def test_factura_con_impuestos(self):
        productos = [("Producto1", 5, 20)]
        # Total = 5*20 = 100
        # Sin descuento -> total_descuento = 100
        # Impuesto del 8%: 100 * 0.08 = 8
        resultado = calcular_total_factura(productos, 0, 8, 0)
        self.assertEqual(resultado, 108)
    
    def test_factura_completa(self):
        productos = [("Producto1", 3, 40), ("Producto2", 2, 60)]
        # Total = 3*40 + 2*60 = 120 + 120 = 240
        # Descuento 5%: 240 * 0.05 = 12  => 240 - 12 = 228
        # Impuesto 10%: 228 * 0.10 = 22.8   => 228 + 22.8 = 250.8
        # Envío: 15
        resultado = calcular_total_factura(productos, 5, 10, 15)
        self.assertAlmostEqual(resultado, 265.8, places=2)

if __name__ == '__main__':
    unittest.main()
