# Creamos la función agregar_productos en paquete 
# (Ref. Clase 9 "Libros" - Ejercicio_Final.py)
# Esta sería como la caja de herramientas

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


""" Ahora se crea la función para listar producots del stock
ya con menos comentarios porque entiendo el proceso 
La forma de listar la obtengo de mi ejercicio de Libros"""

# Agregué una función def ()
def listar_productos(productos):
    if not productos:
        print("No hay productos registrados.")
        return

    print("LISTA DE PRODUCTOS")

    # Aqui va el BONUS de diccionarios anidados (Ref Clase 9 --> Otros_Ejemplos_Dict.py )

    for sku, datos in productos.items():
        nombre = datos["info"]["nombre"]
        familia = datos["info"]["familia"]
        costo = datos["stock"]["costo"]
        cantidad = datos["stock"]["cantidad"]

        print(f"- SKU: {sku}")
        print(f"  Nombre: {nombre}")
        print(f"  Familia: {familia}")
        print(f"  Costo: {costo}")
        print(f"  Stock: {cantidad}")
        print("-" * 30)  # Esto se lo agregué para el formato

