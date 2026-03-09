def main():
    print("Opciones")
    print("1. Numero Primo")
    print("2. Factorial del número")
    print("3. Contar vocales del texto")
    opcion = int(input("Ingrese una opción: "))
    
    if opcion == 1:
        numero = int(input("Ingrese un número: "))
        if numero < 2:
            print(f"{numero} no es un número primo.")
            return
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                print(f"{numero} no es un número primo.")
                return
        print(f"{numero} es un número primo.")
        
    elif opcion == 2:
        numero = int(input("Ingrese un número: "))
        if numero < 0:
            print("El factorial no está definido para números negativos.")
            return
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        print(f"El factorial de {numero} es {factorial}.")
        
    elif opcion == 3:
        texto = input("Ingrese un texto: ")
        vocales = "aeiou"
        contador_total = 0

        print("\nConteo por vocal:")
        for vocal in vocales:
            cantidad = texto.lower().count(vocal)  # cuenta minúsculas y mayúsculas
            contador_total += cantidad
            print(f"  {vocal}: {cantidad}")

        print(f"\nTotal de vocales: {contador_total}")
    
if __name__ == "__main__":
    main()   