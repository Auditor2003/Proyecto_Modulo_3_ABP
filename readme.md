
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
- Inicializar una **lista vacía** para almacenar productos  
- Cada producto se guarda como un **diccionario**

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
> Diicionario anidado en gestion_datos.py Lin 58-62

---

### Lógica de opciones

#### Opción 1: Agregar producto
- Pedir datos del producto:
  - ID (SKU)
  - Familia
  - Nombre
  - Precio
  - Stock
  - Costo
  - Gasto
- Validar los datos ingresados
- Guardar el producto en la lista
- Mostrar mensaje de confirmación

---

#### Opción 2: Listar productos
- Si la lista está vacía:
  - Mostrar mensaje **"No hay productos"**
- Si no:
  - Recorrer la lista
  - Mostrar cada producto en stock

---

#### Opción 3: Buscar producto
- Pedir identificador (ID o SKU)
- Buscar el producto en la lista
- Si existe:
  - Mostrar sus datos
- Si no existe:
  - Mostrar mensaje de error

---

#### Opción 4: Eliminar producto
- Pedir identificador del producto
- Buscar el producto
- Si existe:
  - Eliminarlo de la lista
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
