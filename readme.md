Programa de Control de Stock en Pyhton para implementar Estructuras de Control, Funciones y Manejo de Datos - Proyecto Módulo 3 ABP

Proyecto en Python para gestionar productos usando listas y diccionarios.

Incluye menú interactivo con opciones para agregar, listar, buscar y eliminar productos.

El sistema está organizado en un paquete que contiene módulos para menú, validaciones y gestión de datos

Tecnologías
Python 3

Autor

Diego Muñoz

Mapa Mental de Pseudocódigo

Paso 1. Ejecutar programa
1.1 Mostrar Mensaje de Bienvenida
1.2 Breve explicación de uso del Programa (Sencillo e intuitivo) 

Paso 2. Código del Programa
2.1 INICIALIZAR una lista vacía para guardar productos
Aquí se almacenarán los productos como diccionarios

DEFINIR un menú principal
Opción 1: Agregar producto
Opción 2: Listar productos
Opción 3: Buscar producto
Opción 4: Eliminar producto
Opción 5: Salir

MIENTRAS el usuario NO elije salir:
Mostrar : Menú
Perdir al usuario una opción

" Aquí lo dejo indentado (importante estar debajo o fuera de cada segmento del código
"" Usar la mayor cantidad de funciones estudiadas en clase, modularización de funciones
""" Agregar bonus si es que se puede como diccionarios anidados

SI la opción es "Agregar producto"
        PEDIR datos del producto (id (SKU), familia, nombre, precio, stock, Costo, Gasto)
        VALIDAR los datos ingresados (Validar si existen las categorías para el diccionario)
        GUARDAR almacebar en la lista
        MOSTRAR mensaje de confirmación

    SI la opción es "Listar productos"
        SI la lista está vacía
            MOSTRAR mensaje "No hay productos"
        SI NO
            RECORRER la lista
            MOSTRAR cada producto en Stock

    SI la opción es "Buscar producto"
        PEDIR un identificador (id o SKU)
        BUSCAR el producto en la lista
        SI existe
            MOSTRAR sus datos
        SI NO existe
            MOSTRAR mensaje de error

    SI la opción es "Eliminar producto"
        PEDIR identificador del producto
        BUSCAR el producto
        SI existe
            ELIMINARLO de la lista
            MOSTRAR mensaje de éxito
        SI NO
            MOSTRAR mensaje indicando que no se encontró

    SI la opción es "Salir"
        MOSTRAR mensaje de despedida
        TERMINAR el ciclo

    SI la opción NO es válida
        MOSTRAR mensaje de error
        CONTINUAR el ciclo


