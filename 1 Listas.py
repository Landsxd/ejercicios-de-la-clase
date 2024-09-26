#Dada una lista de palabras, cuenta cuántas veces aparece la palabra "Python" en la lista.

palabras = ["Python", "Java", "C++", "Python", "JavaScript", "Python", "C#"]

contador=0
for palabra in palabras:
    if palabra == "Python":
        contador += 1
print ("aparecen", contador,  "veces") 


#2.- Dada una lista de cadenas de texto, convierte todas las cadenas a mayúsculas sin usar métodos como upper().

frases = ["hola", "mundo", "python", "es", "genial"]

mayusculas=[]
for frase in  frases:
    frase_nueva=""
    for letra in frase:

        if "a" <= letra <= "z":
            frase_nueva += chr(ord(letra)-32)
        else:
            frase_nueva += letra
    mayusculas.append(frase_nueva)
print (mayusculas)

#3.- Dada una lista de palabras, elimina todas aquellas palabras que tengan menos de 4 caracteres.

palabras= ["sol","luna","cielo","mar","estrella","pez"]
palabras_filtradas= [palabra for palabra in palabras if len(palabra)>= 4]
print(palabras_filtradas) 

#4Dada una lista de números, encuentra el número máximo sin usar la función max().

numeros=[15, 22, 8, 34, 9, 6, 17]
maximo=numeros[0]
for numero in numeros:
    if numero > maximo:
        maximo = numero
print(maximo) 

#Dada una lista de números enteros, cuenta cuántos números son positivos.

numeros=[-3, 5, -7, 2, -8, 10, -4, 6]
contador_positivos=sum(1 for numero in numeros if numero > 0)
print(contador_positivos)  

#Dada una lista, invierte el orden de los elementos sin usar métodos como reverse().

numeros=[1, 2, 3, 4, 5]
invertidos=[]
for numero in numeros:
    invertidos.insert(0, numero)  
print(invertidos)  

#Dada una lista de números, encuentra y muestra la media (promedio) de los elementos de la lista.

numeros=[4, 7, 2, 9, 3, 8, 5]
suma=sum(numeros)
media=suma / len(numeros)
print(media) 

numeros = [4, 7, 2, 9, 3, 8, 5]
print(*numeros)
promedio = sum(numeros) / len(numeros)
print(f'el promedio de la lista es {promedio}')




