A=input("Dime un nombre:" )

AES = A.replace(" ", "") #Quita los eeespacios y los convierte en nada para que no cuente los espacios que son caracyeres
num_letras = len(AES)#La etiqueta len cuenta los caracteres y los covierte en un numero

print(f"{A.upper()} tiene {num_letras} letras")