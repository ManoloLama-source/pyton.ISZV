
fecha = input("Ingresa tu fecha de nacimiento (formato dd/mm/aaaa): ")

# Dividir la fecha usando el separador "/"
partes = fecha.split('/') #Divide los texto en base a / y crea tres partes 
#Que luego esas partes cambia si pnes partes[]y va siempre del cero para adelante 

# Mostrar cada parte
print("Día:", partes[0])
print("Mes:", partes[1])
print("Año:", partes[2])