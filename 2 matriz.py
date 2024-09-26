#1.-Escribe un programa que tome dos matrices de igual tamaño (matrices bidimensionales) y devuelva una nueva matriz que sea la suma de las dos matrices originales.

def sumar_matrices(matriz1,matriz2):
    filas=len(matriz1)
    columnas=len(matriz1[0])
    suma=[[0]*columnas for _ in range(filas)]
    
    for i in range(filas):
        for j in range(columnas):
            suma[i][j] = matriz1[i][j] + matriz2[i][j]
    
    return suma
matriz1 = [[1, 2, 3], [4, 5, 6]]
matriz2 = [[7, 8, 9], [10, 11, 12]]
resultado = sumar_matrices(matriz1, matriz2)
print(resultado)  

print("---------------------------------------------")

def multiplicar_matrices(matriz1, matriz2):
    filas1=len(matriz1)
    columnas1=len(matriz1[0])
    filas2=len(matriz2)
    columnas2=len(matriz2[0])
    
    if columnas1!= filas2:
        raise ValueError("el número de columnas de la primera matriz debe coincidir con el número de filas de la segunda.")
    
    producto=[[0]*columnas2 for _ in range(filas1)]
    
    for i in range(filas1):
        for j in range(columnas2):
            for k in range(columnas1):
                producto[i][j] += matriz1[i][k] * matriz2[k][j]
    
    return producto


matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]
resultado = multiplicar_matrices(matriz1, matriz2)
print(resultado)  

print("---------------------------------------------")

def transpuesta_matriz(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    transpuesta=[[0]*filas for _ in range(columnas)]
    
    for i in range(filas):
        for j in range(columnas):
            transpuesta[j][i]=matriz[i][j]
    
    return transpuesta


matriz=[[1, 2, 3], [4, 5, 6]]
resultado=transpuesta_matriz(matriz)
print(resultado)  


print("---------------------------------------------")
def es_cuadrado_magico(matriz):
    n=len(matriz)
    suma_diagonal_principal=sum(matriz[i][i] for i in range(n))
    suma_diagonal_secundaria=sum(matriz[i][n - 1 - i] for i in range(n))
    
    if suma_diagonal_principal!=suma_diagonal_secundaria:
        return False

    for i in range(n):
        if sum(matriz[i])!=suma_diagonal_principal:
            return False
        if sum(matriz[j][i] for j in range(n))!=suma_diagonal_principal:
            return False
            
    return True


matriz = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
resultado = es_cuadrado_magico(matriz)
print(resultado)
