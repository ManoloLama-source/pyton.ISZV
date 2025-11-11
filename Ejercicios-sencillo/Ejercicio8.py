
n = int(input("Introduce el primer número entero (dividendo): "))
m = int(input("Introduce el segundo número entero (divisor): "))


c = n // m #La divion con dos barras se le llama floor division y sirver para redondear para abajo y asi quitar decimales 
r = n % m #Modulus sirve para obtener le resto de la operacion directamente 


print(f"La división de {n} entre {m} da un cociente {c} y un resto {r}")