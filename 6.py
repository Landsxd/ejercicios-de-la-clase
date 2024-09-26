def registrar_alumnos():
    alumnos = []

    while True:
        nombre = input("Ingrese el nombre del alumno (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        
        # Ingresar calificaciones
        calificaciones = []
        while True:
            calificacion = input(f"Ingrese una calificación para {nombre} (o 'fin' para terminar): ")
            if calificacion.lower() == 'fin':
                break
            try:
                calificaciones.append(float(calificacion))
            except ValueError:
                print("Por favor, ingrese un número válido.")

        # Almacenar el nombre y las calificaciones en una tupla
        alumnos.append((nombre, calificaciones))

    return alumnos

def calcular_promedios(alumnos):
    promedios = []
    for nombre, calificaciones in alumnos:
        if calificaciones:  # Evitar división por cero
            promedio = sum(calificaciones) / len(calificaciones)
        else:
            promedio = 0
        promedios.append((nombre, promedio))
    return promedios

def mostrar_alumnos(promedios):
    print("\nTodos los alumnos y sus promedios:")
    for nombre, promedio in promedios:
        print(f"{nombre}: {promedio:.2f}")

def filtrar_alumnos(promedios, condicion, valor):
    print(f"\nAlumnos con promedio {condicion} a {valor}:")
    for nombre, promedio in promedios:
        if (condicion == 'mayor' and promedio >= valor) or (condicion == 'menor' and promedio < valor):
            print(f"{nombre}: {promedio:.2f}")

def main():
    alumnos = registrar_alumnos()
    promedios = calcular_promedios(alumnos)
    
    mostrar_alumnos(promedios)

    # Filtrar por promedio
    while True:
        opcion = input("\n¿Desea filtrar alumnos por promedio? (sí/no): ")
        if opcion.lower() == 'no':
            break
        
        condicion = input("Ingrese 'mayor' para promedios mayores o 'menor' para promedios menores: ")
        valor = float(input("Ingrese el valor de promedio: "))
        
        filtrar_alumnos(promedios, condicion, valor)

if __name__ == "__main__":
    main()
