loto=[1,4,5,6,7]
n=[]

for i in range(len(loto)):
    dato=int(input("Introduzca un sus numero: "))
    n.append(dato)

if(n==loto):
    print("Usted ha ganado la loteria")
else:
    print("Usted ha perdido")
