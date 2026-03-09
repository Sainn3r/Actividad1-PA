def validar_nombre(nombre):
    if len(nombre) < 3:
        print("El nombre debe tener mínimo 3 caracteres.")
        return False
    return True

def validar_edad(edad):
    if edad < 0 or edad > 120:
        print("La edad debe estar entre 0 y 120.")
        return False
    return True

def validar_correo(correo):
    if "@" not in correo:
        print("El correo debe contener @.")
        return False
    if ".com" not in correo and "edu.co" not in correo:
        print("El correo debe contener .com o edu.co")
        return False
    return True

def pedir_estudiante():
    while True:
        nombre = input("Nombre: ")
        if validar_nombre(nombre):
            break

    while True:
        edad = int(input("Edad: "))
        if validar_edad(edad):
            break

    while True:
        correo = input("Correo: ")
        if validar_correo(correo):
            break

    return {"nombre": nombre, "edad": edad, "correo": correo}

def main():
    lista_estudiantes = []

    while True:
        print("1. Agregar estudiante")
        print("2. Ver lista")
        print("3. Salir")
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            estudiante = pedir_estudiante()
            lista_estudiantes.append(estudiante)
            print(f"{estudiante['nombre']} agregado correctamente.")

        elif opcion == 2:
            if not lista_estudiantes:
                print("No hay estudiantes registrados.")
            else:
                print("Lista de estudiantes")
                for e in lista_estudiantes:
                    print(f"  {e['nombre']} | {e['edad']} años | {e['correo']}")

        elif opcion == 3:
            print("Hasta luego ")
            break
        else:
            print(" Opción no válida.")

if __name__ == "__main__":
    main()