"""
Aqui pruebo si funciona la modularización del menú inicial
(Ref. Clase 4 : Ejercicio final.py)
Aquí pruebo la modularización del menú inicial

"""

# Aqui traigo una de la herrameintas de la caja gestion_datos.py
from paquete.gestion_datos import agregar_producto
from paquete.gestion_datos import listar_productos
from paquete.gestion_datos import buscar_producto
from paquete.gestion_datos import eliminar_producto


def mostrar_menu(productos):

    # Ciclo para que el menú se repita hasta que el usuario salga
    # Incluyo la condición booleana TRUE solicitada
    # Hice cambio de los condicionales iniciales des Lista a Diciconarios

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
            buscar_producto(productos) 
        
        elif opcion == "4":
            eliminar_producto(productos)

        elif opcion == "5":
            print("Gracias por usar el Sistema")
            break

        else:
            print("Ingrese una opción válida")

