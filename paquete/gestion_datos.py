# Creamos la función agregar_procutos en paquete (Ref. Calse 9 "Libros" Ejercicio_Final.py)
def agregar_producto(productos):
    print("\nAGREGAR PRODUCTO")

    sku = input("Ingrese SKU: ")
    nombre = input("Ingrese nombre del producto: ")
    familia = input("Ingrese familia: ")

    precio = float(input("Ingrese precio: "))
    cantidad = int(input("Ingrese cantidad en stock: "))

    producto = {
        "sku": sku,
        "info": {
            "nombre": nombre,
            "familia": familia
        },
        "stock": {
            "precio": precio,
            "cantidad": cantidad
        }
    }

    productos.append(producto)
    print("✅ Producto agregado correctamente")
