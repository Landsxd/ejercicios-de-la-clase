import re
#CONMTRASEÑA
def validar_contraseña(contraseña):
    criterios={
        "longitud":len(contraseña) >= 10,
        "mayúscula":re.search(r"[A-Z]", contraseña) is not None,
        "minúscula":re.search(r"[a-z]", contraseña) is not None,
        "número":re.search(r"[0-9]", contraseña) is not None,
        "carácter especial":re.search(r"[!@#$%^&*(),.?\":{}|<>]", contraseña) is not None,
    }

    return criterios

def main():
    contraseña=input("Ingrese una contraseña: ")
    criterios=validar_contraseña(contraseña)

    if all(criterios.values()):
        print("La contraseña es segura.")
    else:
        print("La contraseña no es segura por los siguientes motivos:")
        for criterio, cumple in criterios.items():
            if not cumple:
                print(f"- No cumple con el criterio de {criterio}.")

#TIPO DE CAMBIO
if __name__=="__main__":
    main()


    def obtener_tipos_de_cambio():
     return {
        'USD': {'EUR': 0.85, 'MXN': 20.0},
        'EUR': {'USD': 1.18, 'MXN': 23.5},
        'MXN': {'USD': 0.05, 'EUR': 0.043}
    }

def convertir_moneda(cantidad, moneda_origen, moneda_destino, tipos_de_cambio):
    if moneda_origen in tipos_de_cambio and moneda_destino in tipos_de_cambio[moneda_origen]:
        tasa=tipos_de_cambio[moneda_origen][moneda_destino]
        return cantidad*tasa
    else:
        return None

def main():
    tipos_de_cambio=obtener_tipos_de_cambio()

   
    moneda_origen=input("Ingrese la moneda de origen (USD, EUR, MXN): ").upper()
    cantidad=float(input("Ingrese la cantidad a convertir: "))
    moneda_destino_1=input("Ingrese la primera moneda de destino (USD, EUR, MXN): ").upper()
    moneda_destino_2=input("Ingrese la segunda moneda de destino (USD, EUR, MXN): ").upper()

 
    if moneda_origen not in tipos_de_cambio or moneda_destino_1 not in tipos_de_cambio or moneda_destino_2 not in tipos_de_cambio:
        print("Una o más monedas ingresadas son inválidas.")
        return

   
    resultado_1 = convertir_moneda(cantidad, moneda_origen, moneda_destino_1, tipos_de_cambio)
    resultado_2 = convertir_moneda(cantidad, moneda_origen, moneda_destino_2, tipos_de_cambio)

    
    print(f"{cantidad} {moneda_origen} equivale a {resultado_1:.2f} {moneda_destino_1}.")
    print(f"{cantidad} {moneda_origen} equivale a {resultado_2:.2f} {moneda_destino_2}.")

if __name__ == "__main__":
    main()



def main():
   
    candidatos = {}

    while True:
        
        voto = input("Ingrese el nombre del candidato por el que desea votar (o 'salir' para terminar): ").strip()

        if voto.lower() == 'salir':
            break

       
        if voto in candidatos:
            candidatos[voto] += 1 
            print(f"Voto registrado para {voto}.")
        else:
            
            agregar = input(f"El candidato '{voto}' no existe. ¿Desea agregarlo? (si/no): ").strip().lower()
            if agregar == 'sí':
                candidatos[voto] = 1  
                print(f"El candidato '{voto}' ha sido agregado y se le ha registrado un voto.")
            else:
                print("Voto no registrado.")

   
    print("\nResultados de la votación:")
    for candidato, votos in candidatos.items():
        print(f"{candidato}: {votos} voto(s)")

if __name__ == "__main__":
    main()

