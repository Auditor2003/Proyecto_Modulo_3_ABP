# Función para buscar productos por familia
# Refrencia Clase 9 --> ejercicio_final.py "Recorrido de diccionario de libros para busqueda por familia"
# referencia Clase 3 --> ejercicio_final.py "Uso if not (autos)"

def buscar_por_familia(productos):
    print("BUSCAR PRODUCTOS POR FAMILIA")

    print("Seleccione una familia:")
    print("1. Materias Primas para Producción")
    print("2. Productos Terminados para Venta")
    print("3. Artículos de Oficina")
    print("4. Artículos de Seguridad")
    print("5. Todos los artículos")

    opcion = input("Ingrese una opción: ")

    # Convertimos la opción en texto
    if opcion == "1":
        familia_buscada = "MP"
    elif opcion == "2":
        familia_buscada = "PT"
    elif opcion == "3":
        familia_buscada = "AOF"
    elif opcion == "4":
        familia_buscada = "ADS"
    elif opcion == "5":
        familia_buscada = "TODOS"
        
    else:
        print("Opción de familia inválida")
        return

    print(f"Productos de la familia: {familia_buscada}")
    encontrado = False

    # Recorremos todos los productos
    for sku, datos in productos.items():

        # Si eleje TODOS va por defecto , si no BUSCA por Familia
        
        if familia_buscada == "TODOS" or datos["info"]["familia"] == familia_buscada:
            encontrado = True
            print(f"- SKU: {sku}")
            print(f"  Nombre: {datos['info']['nombre']}")
            print(f"  Familia: {datos['info']['familia']}")
            print(f"  Costo: {datos['stock']['costo']}")
            print(f"  Stock: {datos['stock']['cantidad']}")
            print("-" * 30)

    if not encontrado:
        print("No hay productos en esta familia.")
