"""
factura_original.py
-------------------
Este script genera una factura final a partir de la entrada del usuario:
- Se solicita la cantidad de productos.
- Para cada producto se ingresa nombre, cantidad y precio unitario.
- Se calcula el subtotal de cada producto y el total general.
- Se aplica un descuento (si el usuario dispone de uno).
- Se agregan impuestos y costo de envío.
- Finalmente, se imprime el detalle de la factura.
"""

def main():
    print("Ingrese la cantidad de productos:")
    n = int(input())
    total = 0.0
    productos = []
    
    # Se recogen los datos de los productos y se acumula el total de la compra.
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

    # Se aplica un descuento si el usuario lo indica.
    print("\n¿Tiene código de descuento? (s/n):")
    resp = input().lower()
    descuento = 0.0
    if resp == "s":
        print("Ingrese el porcentaje de descuento:")
        descuento_porcentaje = float(input())
        descuento = total * (descuento_porcentaje / 100)
    total_con_descuento = total - descuento

    # Se aplican los impuestos.
    print("\nIngrese el porcentaje de impuestos a aplicar:")
    impuesto_porcentaje = float(input())
    impuestos = total_con_descuento * (impuesto_porcentaje / 100)

    # Se ingresa el costo de envío.
    print("Ingrese el costo de envío:")
    envio = float(input())

    # Cálculo del total final.
    total_final = total_con_descuento + impuestos + envio

    # Se imprime el detalle de la factura.
    print("\nDetalle de la factura:")
    for prod in productos:
        print(f"Producto: {prod[0]}, Cantidad: {prod[1]}, Precio unitario: {prod[2]}, Subtotal: {prod[3]}")
    print(f"Descuento aplicado: {descuento}")
    print(f"Impuestos: {impuestos}")
    print(f"Envío: {envio}")
    print(f"Total final: {total_final}")

if __name__ == "__main__":
    main()
