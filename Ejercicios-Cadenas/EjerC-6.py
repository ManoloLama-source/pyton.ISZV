# Pedir la frase y la vocal al usuario
frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")

# Convertir la vocal a mayúscula y reemplazarla en la frase
frase_modificada = frase.replace(vocal.lower(), vocal.upper())


print(frase_modificada)