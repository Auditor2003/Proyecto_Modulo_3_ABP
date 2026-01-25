# Creamos la función agregar_productos en paquete
# (Ref. Clase 9 "Libros" - Ejercicio_Final.py)

def agregar_producto(productos):
    # Muestra el título del proceso en pantalla
    print("AGREGAR PRODUCTO")

    # Solicita al usuario el SKU del producto
    sku = input("Ingrese SKU: ")

    # Verifica si el SKU ya existe en el diccionario productos
    if sku in productos:
        print("El SKU ya existe.")
        # Sale de la función sin agregar el producto
        return

    # Solicita los datos generales del producto
    nombre = input("Ingrese nombre del producto: ")
    familia = input("Ingrese familia: ")

    # Solicita y convierte los datos numéricos
    costo = int(input("Ingrese costo: "))
    cantidad = int(input("Ingrese cantidad en stock: "))

    # Agrega el producto al diccionario usando el SKU como clave

    # (Ref Clase 7 --> Ejemplo_lista_diccionario.py y Reapso_diccionario.py)
    productos[sku] = {
        "info": {
            "nombre": nombre,
            "familia": familia
        },
        "stock": {
            "costo": costo,
            "cantidad": cantidad
        }
    }

    # Confirma que el producto fue agregado correctamente
    print("Producto agregado correctamente.")



