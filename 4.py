import math


def saludar(nombre):
    return f"Hola, {nombre}"


def area_circulo(radio):
    return math.pi * (radio ** 2)


def millas_a_kilometros(millas):
    return millas * 1.60934

def repetir_texto(texto, veces):
    return texto * veces

def multiplicar(a, b):
    return a * b


def cambiar_caso(texto):
    return texto.swapcase()


def perimetro_rectangulo(largo, ancho):
    return 2 * (largo + ancho)


def temperatura_media(max_temp, min_temp):
    return (max_temp + min_temp) / 2

def main():
    while True:
        print("\nSeleccione una opción:")
        print("1. Saludo Personalizado")
        print("2. Área de un Círculo")
        print("3. Conversión de Millas a Kilómetros")
        print("4. Repetir Texto")
        print("5. Multiplicación Simple")
        print("6. Mayúsculas y Minúsculas")
        print("7. Calcular Perímetro de un Rectángulo")
        print("8. Calcular Temperatura Media")
        print("9. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            nombre = input("Introduce tu nombre: ")
            print(saludar(nombre))
        
        elif opcion == "2":
            radio = float(input("Introduce el radio del círculo: "))
            print(f"El área del círculo es: {area_circulo(radio):.2f}")

        elif opcion == "3":
            millas = float(input("Introduce la distancia en millas: "))
            print(f"{millas} millas son {millas_a_kilometros(millas):.2f} kilómetros")

        elif opcion == "4":
            texto = input("Introduce el texto: ")
            veces = int(input("¿Cuántas veces quieres repetirlo? "))
            print(repetir_texto(texto, veces))

        elif opcion == "5":
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            print(f"La multiplicación es: {multiplicar(a, b)}")

        elif opcion == "6":
            texto = input("Introduce el texto: ")
            print(cambiar_caso(texto))

        elif opcion == "7":
            largo = float(input("Introduce el largo del rectángulo: "))
            ancho = float(input("Introduce el ancho del rectángulo: "))
            print(f"El perímetro del rectángulo es: {perimetro_rectangulo(largo, ancho)}")

        elif opcion == "8":
            num_dias = int(input("¿Cuántos días deseas introducir? "))
            for _ in range(num_dias):
                max_temp = float(input("Introduce la temperatura máxima: "))
                min_temp = float(input("Introduce la temperatura mínima: "))
                media = temperatura_media(max_temp, min_temp)
                print(f"La temperatura media del día es: {media:.2f}°")
        
        elif opcion == "9":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
