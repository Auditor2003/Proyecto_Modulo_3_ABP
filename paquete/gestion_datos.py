# Creamos la función agregar_productos en paquete 
# (Ref. Clase 9 "Libros" - Ejercicio_Final.py)
# Esta sería como la caja de herramientas

def agregar_producto(productos):
    # Muestra el título del proceso en pantalla
    print("AGREGAR PRODUCTO")
    print("Formato de SKU según tipo de artículo: SKU + 000 (Código)")
    print("MP  - Materias Primas para Producción")
    print("PT  - Productos Terminados para Venta")
    print("AOF - Artículos de Oficina")
    print("ADS - Artículos de Seguridad")
    print("-" * 40)


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
    # podría ser así, pero no me cuesta más --> productos[sku] = {"info": {"nombre": nombre, "familia": familia}, "stock": {"costo": costo, "cantidad": cantidad}}

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

# Función para buscar un producto por SKU

def buscar_producto(productos):
    print("BUSCAR PRODUCTO")

    # Pedimos el SKU a buscar

    sku = input("Ingrese el SKU del producto: ")

    # Verificamos si existe en el diccionario

    if sku in productos:
        print("Producto encontrado:")

        # Accedemos a los datos del producto

        datos = productos[sku]

        print(f"SKU: {sku}")
        print(f"Nombre: {datos['info']['nombre']}")
        print(f"Familia: {datos['info']['familia']}")
        print(f"Costo: {datos['stock']['costo']}")
        print(f"Stock: {datos['stock']['cantidad']}")
    else:
        print("Producto no encontrado.")

# Función para eliminar un producto por SKU

def eliminar_producto(productos):
    print("ELIMINAR PRODUCTO")

    # Pedimos el SKU a eliminar

    sku = input("Ingrese el SKU del producto a eliminar: ")

    # Verificamos si existe

    if sku in productos:
        del productos[sku]   # BORRAMOS el producto

        print("Producto eliminado correctamente.")
    else:
        print("No se encontró el producto.")
