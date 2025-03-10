def contar_subcadena(cadena, subcadena):
    
    contador = cadena.count(subcadena)
    return contador

cadena_principal = input("Ingresa la cadena principal: ")
subcadena_usuario = input("Ingresa la subcadena: ")
num_apariciones = contar_subcadena(cadena_principal, subcadena_usuario)
print(f"La subcadena '{subcadena_usuario}' aparece {num_apariciones} veces en la cadena principal.")
