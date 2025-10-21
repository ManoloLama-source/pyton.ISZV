
correo = input("Introduce tu correo electrónico: ")

# Dividir el correo en dos partes.
correonuv = correo.split('@')[0]#Despues del @ se separa  

# Crear el nuevo correo con dominio ceu.es
nuevo_correo = correonuv + "@ceu.es"

# Mostrar el resultado
print("Tu nuevo correo es:", nuevo_correo)