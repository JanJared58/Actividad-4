def invertir_palabras(frase):

    palabras = frase.split()

    
    palabras_invertidas = [palabra[::-1] for palabra in palabras]


    frase_invertida = ""
    for i in range(len(palabras_invertidas)):
        if i == len(palabras_invertidas) - 1:
            frase_invertida += palabras_invertidas[i]
        else:
            frase_invertida += palabras_invertidas[i] + " "

    return frase_invertida


frase = input("Ingresa una frase: ")
print(f"La frase con las palabras invertidas es: {invertir_palabras(frase)}")
