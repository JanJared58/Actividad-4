def obtener_iniciales(nombre_completo):
    
    palabras = nombre_completo.split()

    iniciales = ""
    for palabra in palabras:
        iniciales += palabra[0].upper()

    return iniciales

nombre = input("Ingresa un nombre completo: ")
print(f"Las iniciales del nombre completo son: {obtener_iniciales(nombre)}")
