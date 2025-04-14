# Proyecto de Refactorización: Cálculo de Descuento

Este repositorio muestra el proceso de refactorización de un sistema para calcular descuentos en función del tipo de cliente (regular, VIP, nuevo). El código inicial contiene redundancias y condiciones complejas, mientras que la versión refactorizada mejora la legibilidad, modularidad y reutilización del código.

## Objetivo

El objetivo del proyecto es:
1. Demostrar cómo identificar y aplicar patrones de refactorización comunes, como la eliminación de código duplicado y la simplificación de condiciones complejas (CA4.1).
2. Comparar las versiones **antes** y **después** de la refactorización, mostrando cómo el código se vuelve más limpio y fácil de mantener.
3. Validar que la refactorización no introduce errores mediante la creación y ejecución de pruebas unitarias (CA4.2).

## Estructura del Proyecto

- **`calculo_descuento_original.py`**: Contiene el código original con condiciones complejas y duplicación de lógica.
- **`calculo_descuento_refactorizado.py`**: Contiene el código refactorizado, donde se aplican patrones como la extracción de método y el renombrado para mejorar la modularidad y legibilidad.
- **`test_calculo_descuento.py`**: Contiene pruebas unitarias (usando `unittest`) para verificar que el comportamiento del cálculo de descuento se mantiene tras la refactorización.

# Proyecto 2 de Refactorización: Cálculo de Factura Final

Este proyecto ilustra un ejemplo más robusto de refactorización en Python, en el que se genera una factura final a partir de datos ingresados por el usuario. El sistema permite:
- Ingresar múltiples productos (nombre, cantidad y precio unitario).
- Aplicar un descuento (si se dispone de un código).
- Calcular y agregar impuestos.
- Incluir un costo de envío.

Se presenta la solución en dos versiones:
- **Código Original:** Un único script monolítico (archivo `factura.py`).
- **Código Refactorizado:** El proceso se divide en funciones auxiliares para mejorar la modularidad, legibilidad y mantenimiento (archivo `factura_refactorizado.py`).

Además, se incluye un conjunto de pruebas unitarias (archivo `test_factura.py`) que validan el cálculo del total final a partir de una función de cálculo sin interactividad, asegurando que la refactorización no introduzca cambios inesperados en el comportamiento.

## Objetivo

- Demostrar la aplicación de varios patrones de refactorización (extracción de métodos, renombrado de variables, eliminación de duplicación, simplificación de condiciones).
- Validar la refactorización mediante pruebas unitarias, comprobando que el sistema se comporta de la misma forma antes y después de la refactorización.

## Estructura del Proyecto

- **`factura_original.py`**: Código original, con toda la lógica en una única función.
- **`factura_refactorizado.py`**: Código refactorizado que utiliza funciones auxiliares para separar responsabilidades.
  - Incluye además la función `calcular_total_factura()` para facilitar las pruebas unitarias.
- **`test_factura.py`**: Archivo de pruebas unitarias (usando `unittest`) para verificar el cálculo del total final de la factura a partir de parámetros de entrada.
  


## Cómo Usar

### 1. Clonar el Repositorio

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/JCSC79/Refactorizaciones-JC.git
cd Refactorizaciones-JC
