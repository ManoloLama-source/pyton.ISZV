A=float(input("Años a invertir: " ))
B=float(input("Cantidad a invertir: "))
C=float(input("Interes anual: "))


Resultado=B*(1+C/100)**A

print(f"El capital que es has conseguido despues de {A} es de {Resultado}")