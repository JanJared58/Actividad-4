def ordenar_por_longitud(lista_palabras):
    
    for i in range(len(lista_palabras)):
        for j in range(len(lista_palabras) - i - 1):
            if len(lista_palabras[j]) > len(lista_palabras[j + 1]):
               
                lista_palabras[j], lista_palabras[j + 1] = lista_palabras[j + 1], lista_palabras[j]

    return lista_palabras


lista_palabras_usuario = input("Ingresa una lista de palabras separadas por comas: ").split(",")
lista_ordenada = ordenar_por_longitud([palabra.strip() for palabra in lista_palabras_usuario])
print(f"La lista ordenada por longitud es: {lista_ordenada}")
