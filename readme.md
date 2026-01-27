
# Programa de Control de Stock en Python  
### Proyecto Módulo 3 – ABP

Proyecto desarrollado en **Python** para gestionar productos, aplicando estructuras de control, funciones y manejo de datos mediante listas y diccionarios.

Incluye un **menú interactivo** con opciones para:
- Agregar productos
- Listar productos
- Buscar productos
- Eliminar productos

El sistema está organizado en un **paquete** que contiene distintos **módulos** para el menú, validaciones y gestión de datos, favoreciendo la modularización y reutilización del código.

---

## Tecnologías utilizadas
- Python 3

---

## Autor
**Diego Muñoz**

---

## Mapa Mental – Pseudocódigo del Sistema

### Paso 1: Ejecutar programa
1. Mostrar mensaje de bienvenida  
2. Breve explicación del uso del programa (sencillo e intuitivo)

---

### Paso 2: Código del programa

#### 2.1 Inicialización
- Inicializar un **diccionario vacío** para almacenar productos  
- Cada producto se guarda como un **diccionario anidado** con información de datos generales y stock/costo

---

### Menú principal
Opciones disponibles:
1. Agregar producto  
2. Listar productos  
3. Buscar producto  
4. Eliminar producto  
5. Salir  

Mientras el usuario **NO elija salir**:
- Mostrar menú  
- Pedir al usuario una opción  

> Se utiliza la mayor cantidad de funciones vistas en clase, modularización del código  
> y como **bonus**, el uso de diccionarios anidados.  
> Diccionario anidado en gestion_datos.py líneas 58-62

---

### Lógica de opciones

#### Opción 1: Agregar producto
- Pedir datos del producto:
  - ID (SKU)
  - Familia
  - Nombre
  - Precio
  - Stock
  - Costo (Gasto)
  
- Validar los datos ingresados
- Guardar el producto en el diccionario
- Si el SKU ya existe, **sumar la cantidad al stock existente**
- Mostrar mensaje de confirmación

---

#### Opción 2: Listar productos
- Si el diccionario está vacío:
  - Mostrar mensaje **"No hay productos"**
- Si no:
  - Recorrer el diccionario
  - Mostrar cada producto en stock con sus datos

---

#### Opción 3: Buscar producto
- Pedir identificador (ID o SKU)
- Buscar el producto en el diccionario
- Si existe:
  - Mostrar sus datos
- Si no existe:
  - Mostrar mensaje de error

---

#### Opción 4: Eliminar producto
- Pedir identificador del producto
- Buscar el producto
- Si existe:
  - Eliminarlo del diccionario
  - Mostrar mensaje de éxito
- Si no:
  - Mostrar mensaje indicando que no se encontró

---

#### Opción 5: Salir
- Mostrar mensaje de despedida
- Terminar el ciclo

---

#### Opción no válida
- Mostrar mensaje de error
- Continuar el ciclo

---

## Identificación de Estructuras y Conceptos Aplicados en el Código

Para facilitar la revisión del proyecto, a continuación se detallan los principales **conceptos y estructuras vistas en clase**, indicando **dónde se aplican dentro del código**.

> La mayoría de estos conceptos se implementan en el módulo  
> **paquete/gestion_datos.py**, que concentra la lógica principal del sistema.

---

### Diccionario
Se utiliza un **diccionario principal** llamado productos, donde cada producto se almacena usando el **SKU como clave**.

- El diccionario productos se recibe como parámetro en las funciones.
- Se accede a los datos mediante claves (productos[sku]).

---

### Diccionario anidado
Cada producto se guarda como un **diccionario que contiene otros diccionarios**, separando información general y datos de stock.

**Ubicación:**  
gestion_datos.py – función agregar_producto()

**Estructura aplicada:**
- info: nombre y familia  
- stock: costo y cantidad

---

### Lista no explícita (recorrido implícito)
El sistema **recorre directamente el diccionario** de productos sin crear listas manualmente.

**Ubicación:**
- listar_productos()
- buscar_por_familia()

**Ejemplo conceptual:**
- Uso de for sku, datos in productos.items()

---

### Set
Se utiliza un **set** para manejar la unicidad de los SKUs existentes.

**Ubicación:**  
gestion_datos.py – función agregar_producto()

**Uso principal:**
- Verificar si un SKU ya existe antes de agregar un producto nuevo.

---

### Tupla
Se utiliza una **tupla** para definir las familias válidas de productos.

**Ubicación:**  
gestion_datos.py – función agregar_producto()

**Motivo:**
- Estructura inmutable utilizada para validaciones.

---

### Validaciones simples
Se aplican validaciones básicas como:

- Verificar si el diccionario está vacío  
- Verificar si un SKU existe  
- Validar que la familia ingresada sea correcta  

**Ubicación principal:**  
gestion_datos.py

---

### Condicionales (if / elif / else)
Se utilizan estructuras condicionales para controlar el flujo del programa según:

- Opciones del menú
- Existencia de datos
- Confirmaciones del usuario

**Ubicación:**
- menu.py
- gestion_datos.py
- funciones_utiles.py

---

### Manejo de errores (try / except)
Se implementa manejo de errores para evitar que el programa se detenga ante ingresos incorrectos de datos numéricos.

**Ubicación:**  
gestion_datos.py – función agregar_producto()

**Uso principal:**
- Validar costo y cantidad ingresados por el usuario.

---

## Mejoras Futuras

- Permitir que un mismo SKU pueda ingresarse con **diferentes costos** y cantidades (partidas múltiples)  
- Listar todas las partidas de un SKU para un control detallado de inventario  
- Agregar función para calcular **costo promedio ponderado** 

- Esta mejora permitirá reflejar mejor los cambios de costos históricos sin afectar el stock actual

- Se considerará realizar cambio para eliminar productos por partida o cantidades unitarias. De momento solo elimina SKU total
