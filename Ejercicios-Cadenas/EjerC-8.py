
precio = input("Precio en euros (ej: 12.34): ")

# Separar en euros y céntimos
euros= precio.split('.')[0]#antes del punto
centimos=precio.split('.')[1]#después del punto

print("Euros:", euros)
print("Céntimos:", centimos)