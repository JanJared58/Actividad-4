def cifrado_cesar(cadena, desplazamiento):
    resultado = ""
    
    for char in cadena:
        if char.isalpha():  
            
            inicio = ord('A') if char.isupper() else ord('a')
            
            nuevo_char = chr((ord(char) - inicio + desplazamiento) % 26 + inicio)
            resultado += nuevo_char
        else:
            
            resultado += char

    return resultado

cadena_usuario = input("Ingresa una cadena: ")
desplazamiento_usuario = int(input("Ingresa el desplazamiento: "))
cadena_cifrada = cifrado_cesar(cadena_usuario, desplazamiento_usuario)
print(f"La cadena cifrada es: {cadena_cifrada}")
