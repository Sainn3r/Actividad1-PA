def main():
    valor = float(input("Introduce el precio: "))
    iva = valor * 0.19
    descuento = valor * 0.10
    if valor >= 200000:
        valor_final = valor + iva - descuento
        print("El precio final es: $", valor_final)
    else:
        valor_final = valor + iva
        print("El precio final con IVA es: $", valor_final)  

if __name__ == "__main__":
    main()