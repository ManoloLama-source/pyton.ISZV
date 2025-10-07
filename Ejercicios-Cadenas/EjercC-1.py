# Solicitar el nombre del usuario
nombre = input("¿Cuál es tu nombre? ")

# Solicitar un número entero
numero = int(input("¿Cuántas veces quieres que repita tu nombre? "))

# Imprimir el nombre tantas veces como el número introducido
for i in range(numero):#For i es un bucque que con range y el inoput hace que se repita
    print(nombre)