def fusionar_listas_ordenadas(lista1, lista2):

    lista_fusionada = sorted(lista1 + lista2)
    return lista_fusionada

lista1 = [1, 3, 5, 7]
lista2 = [2, 4, 6, 8]
lista_fusionada = fusionar_listas_ordenadas(lista1, lista2)
print(f"La lista fusionada y ordenada es: {lista_fusionada}")
