def crear_tupla(num1, num2, num3):
    return (num1, num2, num3)

# Ejemplo de uso
resultado = crear_tupla(1, 2, 3)
print(resultado) 

numeros = (10, 20, 30, 40, 50)
tercer_elemento = numeros[2]  
print(tercer_elemento)  


# Definición de las tuplas
pares = (0, 2, 4, 6, 8)
impares = (1, 3, 5, 7, 9)

# Concatenación de las tuplas
resultado = pares + impares

# Mostrar el resultado
print(resultado)  


colores = ('rojo', 'azul', 'verde', 'rojo', 'amarillo', 'rojo')

# Contar cuántas veces aparece "rojo"
contador_rojo = colores.count('rojo')

# Imprimir el resultado
print(contador_rojo)  


nombres = ['Ana', 'Juan', 'Pedro', 'Luis']

# Convertir la lista en una tupla
tupla_nombres = tuple(nombres)

# Mostrar la tupla resultante
print(tupla_nombres)  


tupla_larga = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Crear una nueva tupla con los primeros 5 elementos
tupla_primeros_cinco = tupla_larga[:5]

# Mostrar la nueva tupla
print(tupla_primeros_cinco) 


# Inicialización de las variables
a = 5
b = 10

# Intercambio utilizando una tupla
a, b = b, a

# Mostrar los resultados
print("a:", a)  
print("b:", b)  
