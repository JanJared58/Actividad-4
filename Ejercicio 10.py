def eliminar_no_pares(lista):

    lista_pares = [num for num in lista if num % 2 == 0]
    return lista_pares


lista_usuario = input("Por favor, ingresa una lista de números separados por comas: ").split(",")
lista_usuario = [int(num) for num in lista_usuario] 
lista_pares = eliminar_no_pares(lista_usuario)
print(f"La lista con solo los elementos pares es: {lista_pares}")
