
nombre = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio unitario: "))
unidades = int(input("Introduce el número de unidades: "))

# Calcular el coste unitario
coste_total = precio * unidades

# 
partes = [#lista de partes que luego se unen
    f"{nombre}:",
    f"{precio:6.2f} € ",#Espacio total 6, dos decimales que se ponen con .2f
    f"Unidades: {unidades:03d} ",#Tres digitos con ceros a la izquierda si es necesario
    f"Coste total: {coste_total:8.2f} €"
]

# Unir todo con espacios en este caso o con comas si se quiere
resultado = " ".join(partes)
print(resultado)