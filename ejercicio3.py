def main():
    numero_inicio = int(input("número de inicio: "))
    numero_iteraciones = int(input("número de iteraciones: "))
    
    if numero_iteraciones <= 0:
        print("El número de iteraciones no puede ser negativo.")
        return
    
    serie = []
    a=1
    b=1
    
    for i in range(numero_inicio-1):
        a, b = b, a + b
    
    for i in range(numero_iteraciones):
        serie.append(a)
        a, b = b, a + b

    print("Serie de Fibonacci:")
    print(serie)
    print("Terminos totales:", len(serie))
    print("Ultimo termino: ", serie[-1])
    
if __name__ == "__main__":
    main()