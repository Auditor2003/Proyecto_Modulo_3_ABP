# Aqui pruebo si funciona la modularización del menú inicial

def mostrar_menu(productos):
    print("MENÚ PRINCIPAL")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "5":
        print("Gracias por usar el sistema")
    else:
        print("Ingrese una función válida")
