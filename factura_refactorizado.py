"""
factura_refactorizado.py
------------------------
Este script genera la factura final de una compra aplicando buenas prácticas de refactorización:
- Se extrae la entrada de datos en una función separada.
- Se crea una función para aplicar el descuento.
- Se dispone de funciones para calcular impuestos y armar la factura.
Cada función tiene una responsabilidad única, lo que mejora la legibilidad y mantenibilidad.
"""

def obtener_productos():
    """
    Solicita al usuario los datos de los productos y retorna una lista de tuplas
    (nombre, cantidad, precio_unitario, subtotal) y el total de la compra.
    """
    print("Ingrese la cantidad de productos:")
    n = int(input())
    total = 0.0
    productos = []
    
    for i in range(n):
        print(f"\nProducto {i+1}:")
        print("Ingrese el nombre del producto:")
        nombre = input()
        print("Ingrese la cantidad:")
        cantidad = int(input())
        print("Ingrese el precio unitario:")
        precio_unitario = float(input())
        subtotal = cantidad * precio_unitario
        productos.append((nombre, cantidad, precio_unitario, subtotal))
        total += subtotal
    return productos, total

def aplicar_descuento(total):
    """
    Pregunta si existe un descuento y, de ser así, lo aplica al total.
    Retorna el total con descuento aplicado y el monto del descuento.
    """
    print("\n¿Tiene código de descuento? (s/n):")
    resp = input().lower()
    descuento = 0.0
    if resp == "s":
        print("Ingrese el porcentaje de descuento:")
        descuento_porcentaje = float(input())
        descuento = total * (descuento_porcentaje / 100)
    total_con_descuento = total - descuento
    return total_con_descuento, descuento

def calcular_impuestos(total, impuesto_porcentaje):
    """
    Calcula los impuestos a aplicar según el porcentaje ingresado.
    """
    return total * (impuesto_porcentaje / 100)

def obtener_envio():
    """
    Solicita el costo de envío al usuario.
    """
    print("Ingrese el costo de envío:")
    return float(input())

def imprimir_factura(productos, descuento, impuestos, envio, total_final):
    """
    Imprime el detalle de la factura.
    """
    print("\nDetalle de la factura:")
    for prod in productos:
        print(f"Producto: {prod[0]}, Cantidad: {prod[1]}, Precio unitario: {prod[2]}, Subtotal: {prod[3]}")
    print(f"Descuento aplicado: {descuento}")
    print(f"Impuestos: {impuestos}")
    print(f"Envío: {envio}")
    print(f"Total final: {total_final}")

def calcular_factura_final():
    """
    Función principal que integra el proceso de la factura.
    Retorna el total final calculado.
    """
    # Obtener productos y total sin descuento
    productos, total = obtener_productos()
    
    # Aplicar descuento
    total_con_descuento, descuento = aplicar_descuento(total)
    
    # Calcular impuestos
    print("\nIngrese el porcentaje de impuestos a aplicar:")
    impuesto_porcentaje = float(input())
    impuestos = calcular_impuestos(total_con_descuento, impuesto_porcentaje)
    
    # Obtener costo de envío
    envio = obtener_envio()
    
    # Calcular total final
    total_final = total_con_descuento + impuestos + envio
    imprimir_factura(productos, descuento, impuestos, envio, total_final)
    return total_final

def main():
    try:
        calcular_factura_final()
    except ValueError:
        print("Error: por favor, ingrese valores numéricos válidos.")

# ...otras funciones como obtener_productos, aplicar_descuento, etc...

def calcular_total_factura(productos, descuento_porcentaje, impuesto_porcentaje, costo_envio):
    """
    Calcula el total final de la factura a partir de:
      - productos: lista de tuplas (nombre, cantidad, precio_unitario)
      - descuento_porcentaje: porcentaje a descontar del total
      - impuesto_porcentaje: porcentaje de impuestos a aplicar
      - costo_envio: costo de envío
    Retorna el total final calculado.
    """
    total = 0.0
    for prod in productos:
        # Cada prod es (nombre, cantidad, precio_unitario)
        subtotal = prod[1] * prod[2]
        total += subtotal

    descuento = total * (descuento_porcentaje / 100)
    total_descuento = total - descuento
    impuestos = total_descuento * (impuesto_porcentaje / 100)
    total_final = total_descuento + impuestos + costo_envio
    return total_final


if __name__ == "__main__":
    main()
