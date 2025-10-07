barras = int(input("Introduce el número de barras no frescas vendidas: "))
precio_normal = 3.49
descuento = 0.60  

precio_descuento = precio_normal * (1 - descuento)
total = barras * precio_descuento

print(f"\nPrecio habitual: {precio_normal}€")
print(f"Descuento: {descuento * 100}%")
print(f"Coste final total: {total:.2f}€")#Lleva dos decimales  