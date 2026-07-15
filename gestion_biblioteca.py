def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        opcion = input("Ingrese una opción (1-6): ").strip()
        if opcion.isdigit():
            opcion_num = int(opcion)
            if 1 <= opcion_num <= 6:
                return opcion_num
        print("Opción no válida. Intente nuevamente.")

def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_copias(copias_texto):
    if not copias_texto.isdigit():
        return False
    copias = int(copias_texto)
    return copias >= 0

def validar_prestamo(prestamo_texto):
    if not prestamo_texto.isdigit():
        return False
    prestamo = int(prestamo_texto)
    return prestamo > 0

def agregar_libro(lista_libros):
    titulo = input("Título del libro: ")
    copias_texto = input("Cantidad de copias: ")
    prestamo_texto = input("Período de préstamo (días): ")
    valido = True
    if not validar_titulo(titulo):
        print("Error: el título no puede estar vacío ni ser solo espacios.")
        valido = False
    if not validar_copias(copias_texto):
        print("Error: las copias deben ser un número entero mayor o igual que cero.")
        valido = False
    if not validar_prestamo(prestamo_texto):
        print("Error: el período de préstamo debe ser un número entero mayor que cero.")
        valido = False
    if not valido:
        return
    libro = {
        "titulo": titulo.strip(),
        "copias": int(copias_texto),
        "prestamo": int(prestamo_texto),
        "disponible": False,
    }
    lista_libros.append(libro)
    print(f"Libro '{libro['titulo']}' registrado correctamente.")

def buscar_libro(lista_libros, titulo_buscar):
    for indice, libro in enumerate(lista_libros):
        if libro["titulo"] == titulo_buscar:
            return indice
    return -1

def actualizar_disponibilidad(lista_libros):
    for libro in lista_libros:
        libro["disponible"] = libro["copias"] >= 1
    print("Disponibilidad actualizada para todos los libros.")

def mostrar_libros(lista_libros):
    actualizar_disponibilidad(lista_libros)
    print("=== LISTA DE LIBROS ===")
    if not lista_libros:
        print("No hay libros registrados.")
        return

    for libro in lista_libros:
        estado = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
        print(f"Título: {libro['titulo']}")
        print(f"Copias: {libro['copias']}")
        print(f"Préstamo: {libro['prestamo']}")
        print(f"Estado: {estado}")
        print("********************************************")
