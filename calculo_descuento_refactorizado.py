"""
Refactorización realizada (CA4.1):

- Aplicado el patrón "Extracción de Método": se movió el cálculo del precio final a una función separada `calcular_precio_final()`.
- Aplicado el patrón "Renombrado": se mejoraron los nombres de las variables para hacerlas más descriptivas (`precio`, `descuento` → `precio_base`, `porcentaje_descuento`, etc.).
- Se mejoró la legibilidad general del código, facilitando su mantenimiento y reutilización.
"""

def calcular_precio_final(precio_base, porcentaje_descuento):
    """Calcula el precio final tras aplicar el descuento."""
    descuento = precio_base * (porcentaje_descuento / 100)
    precio_final = precio_base - descuento
    return precio_final

def main():
    try:
        precio_base = float(input("Introduce el precio base del producto: "))
        porcentaje_descuento = float(input("Introduce el porcentaje de descuento: "))

        if porcentaje_descuento < 0 or porcentaje_descuento > 100:
            print("El porcentaje de descuento debe estar entre 0 y 100.")
            return

        precio_final = calcular_precio_final(precio_base, porcentaje_descuento)
        print(f"El precio final tras el descuento es: {precio_final:.2f}€")

    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")

if __name__ == "__main__":
    main()
