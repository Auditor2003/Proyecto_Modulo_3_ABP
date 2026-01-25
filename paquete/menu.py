"""
Aqui pruebo si funciona la modularización del menú inicial
(Ref. Clase 4 : Ejercicio final.py)
Aquí pruebo la modularización del menú inicial

"""

def mostrar_menu(productos):

    # Ciclo para que el menú se repita hasta que el usuario salga
    # Incluyo la condición booleana TRUE solicitada

    while True:
        print("\nMENÚ PRINCIPAL")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("agregar producto al Sistema")

        elif opcion == "2":
            print("Lista de productos en Stock")

        elif opcion == "3":
            print("Buscar producto en Stock")

        elif opcion == "4":
            print("Eliminar producto del Sistema")

        elif opcion == "5":
            print("Gracias por usar el Sistema")
            break

        else:
            print("Ingrese una opción válida")

