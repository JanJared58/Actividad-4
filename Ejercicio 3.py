def contar_vocales_consonantes(palabra):

    vocales = "aeiouAEIOU"
    
    num_vocales = 0
    num_consonantes = 0
    
    for letra in palabra:
        if letra.isalpha(): 
            if letra in vocales:
                num_vocales += 1
            else:
                num_consonantes += 1

    return num_vocales, num_consonantes


palabra = input("Ingresa una palabra: ")
vocales, consonantes = contar_vocales_consonantes(palabra)
print(f"La palabra '{palabra}' contiene {vocales} vocales y {consonantes} consonantes.")
