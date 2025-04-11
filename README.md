# Proyecto de Refactorización: Cálculo de Descuento

Este repositorio muestra el proceso de refactorización de un sistema para calcular descuentos en función del tipo de cliente (regular, VIP, nuevo). El código inicial contiene redundancia y condiciones complejas, mientras que la versión refactorizada mejora la legibilidad, modularidad y reutilización.

## **Objetivo**

El objetivo del proyecto es:
1. Demostrar cómo identificar y aplicar patrones de refactorización comunes, como la eliminación de código duplicado y la simplificación de condiciones complejas.
2. Comparar las versiones **antes** y **después** de la refactorización, mostrando cómo el código se vuelve más limpio y fácil de mantener.

## **Estructura del Proyecto**

- **`calculo_descuento_original.py`**: Contiene el código original con condiciones complejas y duplicación de código.
- **`calculo_descuento_refactorizado.py`**: Contiene el código después de la refactorización, donde se aplican patrones de refactorización como la eliminación de duplicación y la simplificación de condiciones.
- **`test_calculo_descuento.py`** (Opcional): Contiene pruebas unitarias para verificar que ambas versiones del código calculen correctamente los descuentos.

## **Cómo Usar**

### **1. Clonar el Repositorio**

Primero, clona este repositorio a tu máquina local



## CA4.1 - Identificación y aplicación de patrones de refactorización

Se trabajó con el archivo `calculo_descuento_original.py` y se refactorizó creando una versión más clara y modular: `calculo_descuento_refactorizado.py`.

### Patrones aplicados:
- **Extracción de método**: se movió el cálculo del precio con descuento a una función llamada `calcular_precio_final()`.
- **Renombrado de variables**: se usaron nombres más expresivos para mejorar la legibilidad.
- **Control de errores más claro** y validación de entrada de usuario.

Este cambio se puede ver en el commit: `CA4.1 - Refactorización: extracción de método y renombrado de variables`
