estudiantes = []
contador = 0
banderaSalir = True

print("Sistema de gestion de estudiantes")


def buscar_estudiante(id_buscar):
    for estudiante in estudiantes:
        if estudiante["id"] == id_buscar:
            return estudiante
    return None


def agregar_estudiante():
    global contador

    id_estudiante = input("Ingrese el numero de identificacion: ")

    if buscar_estudiante(id_estudiante) is not None:
        print("Error: ese estudiante ya esta registrado.")
        return

    nombre = input("Ingrese el nombre del estudiante: ")

    try:
        edad = int(input("Ingrese la edad del estudiante: "))
        if edad <= 0:
            print("La edad debe ser mayor que cero.")
            return
    except ValueError:
        print("Debe ingresar una edad numerica.")
        return

    programa = input("Ingrese el programa que estudia: ")

    estudiante = {
        "id": id_estudiante,
        "nombre": nombre,
        "edad": edad,
        "programa": programa
    }

    estudiantes.append(estudiante)
    contador += 1

    print("Estudiante agregado correctamente.")


def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        print("\n--- Lista de estudiantes ---")

        for estudiante in estudiantes:
            print("Identificacion:", estudiante["id"])
            print("Nombre:", estudiante["nombre"])
            print("Edad:", estudiante["edad"])
            print("Programa:", estudiante["programa"])
            print("-------------------------")


def consultar_estudiante():
    id_buscar = input("Ingrese la identificacion del estudiante: ")

    estudiante = buscar_estudiante(id_buscar)

    if estudiante is not None:
        print("\n--- Datos del estudiante ---")
        print("Identificacion:", estudiante["id"])
        print("Nombre:", estudiante["nombre"])
        print("Edad:", estudiante["edad"])
        print("Programa:", estudiante["programa"])
    else:
        print("No se encontro un estudiante con esa identificacion.")


# MENU PRINCIPAL
while banderaSalir:
    print("\n--- SISTEMA DE GESTION DE ESTUDIANTES ---")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        agregar_estudiante()

    elif opcion == "2":
        mostrar_estudiantes()

    elif opcion == "3":
        consultar_estudiante()

    elif opcion == "4":
        banderaSalir = False
        print("Gracias por utilizar el sistema.")

    else:
        print("Opcion no valida. Intente nuevamente.")