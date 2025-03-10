def contar_palabras(texto):
    
    palabras = texto.split()

    num_palabras = len(palabras)

    return num_palabras

texto = input("Ingresa un texto: ")

print(f"El número de palabras en el texto es: {contar_palabras(texto)}")
