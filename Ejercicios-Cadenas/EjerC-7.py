
correo = input("Introduce tu correo electrónico: ")

# Dividir el correo en dos partes.
nombre = correo.split('@')[0]

# Crear el nuevo correo con dominio ceu.es
nuevo_correo = nombre + "@ceu.es"

# Mostrar el resultado
print("Tu nuevo correo es:", nuevo_correo)