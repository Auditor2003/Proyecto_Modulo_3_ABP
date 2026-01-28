
# Programa de Control de Stock en Python
### Proyecto Módulo 3 – ABP

Proyecto desarrollado en **Python** para la gestión de productos en stock, aplicando estructuras de control, funciones y manejo de datos mediante diccionarios.

El sistema incluye un **menú interactivo** que permite:
- Agregar productos
- Listar productos
- Buscar productos
- Eliminar productos

El código está organizado en un **paquete modular**, separando la lógica del menú, la gestión de datos y las funciones de apoyo, favoreciendo la claridad y reutilización del código.

---

## Tecnologías utilizadas
- Python 3

---

## Autor
**Diego Muñoz**

---

## Descripción General del Funcionamiento

Al ejecutar el programa:
1. Se muestra un mensaje inicial y el menú principal.
2. El sistema inicializa un **diccionario vacío** para almacenar los productos.
3. El usuario interactúa con el menú hasta que decide salir del programa.

Cada producto se almacena utilizando un **diccionario anidado**, separando la información general del producto y los datos de stock.

---

## Menú Principal

Opciones disponibles:
1. Agregar producto
2. Listar productos
3. Buscar producto
4. Eliminar producto
5. Salir

El menú se ejecuta dentro de un ciclo que se mantiene activo hasta que el usuario selecciona la opción de salida.

---

## Lógica de las Opciones

### Agregar producto
- Solicita los datos del producto (SKU, nombre, familia, costo y cantidad).
- Valida que la familia ingresada sea correcta.
- Valida el ingreso de datos numéricos mediante try / except.
- Si el SKU ya existe, se **suma la cantidad al stock existente**.
- Si el SKU no existe, se crea un nuevo registro en el diccionario.

---

### Listar productos
- Si no existen productos registrados, se muestra un mensaje informativo.
- En caso contrario, se recorren los productos y se muestran sus datos.

---

### Buscar productos
- Permite buscar productos según su **familia**.
- Existe la opción de mostrar **todos los productos** registrados.

---

### Eliminar producto
- Solicita el SKU del producto.
- Muestra información básica antes de eliminar.
- Solicita confirmación al usuario.
- La eliminación se realiza a nivel de **SKU completo**.

---

## Estructuras y Conceptos Aplicados

- **Diccionario:** estructura principal para almacenar los productos, usando el SKU como clave.
- **Diccionarios anidados:** separación de información general y datos de stock.
- **Tupla:** definición de familias válidas de productos.
- **Set:** verificación de unicidad de los SKUs existentes.
- **Condicionales:** control del flujo del programa y validaciones.
- **Manejo de errores (try / except):** validación de datos numéricos ingresados por el usuario.

La estructura del sistema se basa principalmente en diccionarios, por lo que no se utilizan métodos de listas como .append() o .remove(), ya que su uso no era necesario para el diseño propuesto y la lógica principal del sistema se concentra en el módulo gestion_datos.py, mientras que el menú y las funciones de apoyo se encuentran modularizadas en archivos independientes.

---

## Mejoras Futuras

- Permitir el manejo de múltiples partidas por SKU con distintos costos.
- Calcular costo promedio ponderado.
- Implementar rebaja de stock por venta de unidades.
- Permitir eliminación parcial de stock en lugar de eliminación total del SKU.