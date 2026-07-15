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
