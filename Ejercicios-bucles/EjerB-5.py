

#cream0s tres variable para los datos
cantidad = float(input("¿Cantidad a invertir? "))
interes_anual = float(input("¿Interés porcentual anual? "))
años = int(input("¿Número de años? "))


for i in range(1,años+1):
    cantidad= cantidad * (1 + interes_anual / 100)

print(f"Capital tras el año {i}: {cantidad:.2f}€")