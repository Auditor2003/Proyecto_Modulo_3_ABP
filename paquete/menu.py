"""
Aqui pruebo si funciona la modularización del menú inicial
(Ref. Clase 4 : Ejercicio final.py)
Aquí pruebo la modularización del menú inicial

"""

# Aqui traigo una de la herrameintas de la caja gestion_datos.py
from paquete.gestion_datos import agregar_producto
from paquete.gestion_datos import listar_productos


def mostrar_menu(productos):

    # Ciclo para que el menú se repita hasta que el usuario salga
    # Incluyo la condición booleana TRUE solicitada

    while True:
        print("MENÚ PRINCIPAL")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto(productos)

        elif opcion == "2":
            listar_productos(productos)

        elif opcion == "3": 
            print("Buscar producto en Stock") 
        
        elif opcion == "4": 
            print("Eliminar producto del Sistema")

        elif opcion == "5":
            print("Gracias por usar el Sistema")
            break

        else:
            print("Ingrese una opción válida")

