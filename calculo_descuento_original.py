class Cliente:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

def calcular_descuento_cliente(tipo_cliente, monto):
    if tipo_cliente == "regular":
        if monto > 1000:
            return monto * 0.05
        else:
            return monto * 0.02
    elif tipo_cliente == "vip":
        if monto > 1000:
            return monto * 0.10
        else:
            return monto * 0.05
    elif tipo_cliente == "nuevo":
        if monto > 1000:
            return monto * 0.03
        else:
            return monto * 0.01
    else:
        return 0

def procesar_pago(cliente, monto):
    descuento = calcular_descuento_cliente(cliente.tipo, monto)
    total_a_pagar = monto - descuento
    print(f"El total a pagar por {cliente.nombre} es {total_a_pagar}")

# Ejemplo de uso:
cliente = Cliente("Juan", "vip")
monto = 1500
procesar_pago(cliente, monto)
