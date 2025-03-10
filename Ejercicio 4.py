def eliminar_espacios(cadena):
    
    palabras = cadena.split()

    cadena_sin_espacios_redundantes = " ".join(palabras)

    return cadena_sin_espacios_redundantes


cadena_usuario = input("Ingresa una cadena con espacios adicionales: ")
cadena_sin_espacios = eliminar_espacios(cadena_usuario)
print(f"La cadena sin espacios redundantes es: '{cadena_sin_espacios}'")
