Asignaturas=[]
notas=[]
cont=0
while cont != 10:
    dato1=input("Introduzca sus asignaturas: ")
    Asignaturas.append(dato1)
    dato2=int(input("Introduzca su nota: "))
    notas.append(dato2)
    cont += 1
for i in range(len(Asignaturas)):
    print(f"En {Asignaturas[i]} has sacado {notas[i]}")