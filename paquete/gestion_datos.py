# Creamos la función agregar_productos en paquete 
# (Ref. Clase 9 "Libros" - Ejercicio_Final.py)
# Esta sería como la caja de herramientas

def agregar_producto(productos):
    # Muestra el título del proceso en pantalla
    print("AGREGAR PRODUCTO")

    # Separador visual idea traida de Markdown
    print("-" * 60)

    print("Formato de SKU según tipo de artículo: SKU + 000 (Ej: MP001)")
    print("Familia --> SKU = MP -> Materias Primas para Producción")
    print("Familia --> SKU = PT -> Productos Terminados para Venta")
    print("Familia --> SKU = AOF -> Artículos de Oficina")
    print("Familia --> SKU = ADS -> Artículos de Seguridad")

    # Separador visual idea traida de Markdown
    print("-" * 60)

    # Tupla de familias válidas (estructura inmutable)
    FAMILIAS = ("MP", "PT", "AOF", "ADS")

    # SET para manejar SKUs únicos (no reemplaza al diccionario principal, sería complemento)
    # Ref uso SET Clase 8 --> Ejercicio mi_set.py 

    skus_existentes = set(productos.keys())

    # Solicita al usuario el SKU del producto
    sku = input("Ingrese SKU: ")

    # Verifica si el SKU ya existe en el diccionario productos
    if sku in skus_existentes:
        print("El producto ya existe. Se agregará stock adicional.")

        # Pide la cantidad extra a agregar
        # Agregamos una verificación Try-Except para verificar error de ingreso (Ref. Clase 7 --> temperatura_ejemplo.py)
        try:
            cantidad_extra = int(input("Ingrese cantidad a sumar al stock: "))
            productos[sku]["stock"]["cantidad"] += cantidad_extra
            print(f"Stock actualizado correctamente. Nueva cantidad: {productos[sku]['stock']['cantidad']}")
        except ValueError:
            print("Cantidad inválida. No se actualizó el stock.")
        
        # Salimos de la función después de sumar
        return

    # Solicita los datos generales del producto

    nombre = input("Ingrese nombre del producto: ")
    familia = input("Ingrese familia (MP-PT-AOF-ADS): ")

    # Validación de familia usando tupla
    if familia not in FAMILIAS:
        print("Familia inválida. Producto no agregado.")
        return

    # Solicita y revisa los datos numéricos
    # Se usa float para calcular a futuro PMP (Costo Medio Ponderado)

    try:
        costo = float(input("Ingrese costo: "))
        cantidad = int(input("Ingrese cantidad en stock: "))
    except ValueError:
        print("Error: costo o cantidad inválida. Producto no agregado.")
        return

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

    # Verificamos si el SKU existe en el diccionario
    if sku in productos:
        # Mostramos información básica antes de eliminar (feedback al usuario)
        print(f"Producto encontrado: {productos[sku]['info']['nombre']}")

        # Confirmación para evitar errores
        # Usamos lower (s/n) para validar si estamos seguros de eliminar (Ref. Clase 4 --> ejercicio livecoding_cine.py)   
        confirmacion = input("¿Está seguro que desea eliminarlo? (s/n): ").lower()

        if confirmacion == "s":
            # Eliminamos el producto usando del
            del productos[sku]
            print("Producto eliminado correctamente.")
        else:
            print("Eliminación cancelada.")
    else:
        # Si el SKU no existe
        print("El SKU ingresado no existe.")
