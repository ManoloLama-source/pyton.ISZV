cantidad = int(input("Introduce una cantidad entera de euros: "))

m10 = cantidad // 10
resto = cantidad % 10

m5 = resto // 5
resto = resto % 5

m2 = resto // 2
resto = resto % 2

m1 = resto // 1

total = m10 + m5 + m2 + m1

print("Mínimo de monedas necesarias:", total)
print("Monedas de 10:", m10)
print("Monedas de 5:", m5)
print("Monedas de 2:", m2)
print("Monedas de 1:", m1)


#un buclee que pregunte diez numeros y que diga el menor el mayor y la suma de los diez