# calculo_descuento_refactorizado.py

class Cliente:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

def obtener_descuento(tipo_cliente, monto):
    """
    Devuelve el descuento a aplicar según el tipo de cliente y el monto.
    """
    if tipo_cliente == "regular":
        return monto * 0.05 if monto > 1000 else monto * 0.02
    elif tipo_cliente == "vip":
        return monto * 0.10 if monto > 1000 else monto * 0.05
    elif tipo_cliente == "nuevo":
        return monto * 0.03 if monto > 1000 else monto * 0.01
    else:
        return 0

def calcular_descuento_cliente(tipo_cliente, monto):
    # Mantiene la interfaz original, pero delega en la función auxiliar.
    return obtener_descuento(tipo_cliente, monto)

def procesar_pago(cliente, monto):
    descuento = calcular_descuento_cliente(cliente.tipo, monto)
    total_a_pagar = monto - descuento
    print(f"El total a pagar por {cliente.nombre} es {total_a_pagar}")

# Ejemplo de uso:
if __name__ == "__main__":
    cliente = Cliente("Juan", "vip")
    monto = 1500
    procesar_pago(cliente, monto)
