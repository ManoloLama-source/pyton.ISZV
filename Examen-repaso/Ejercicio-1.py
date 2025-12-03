print("1.Ver saldo \n","2.reintegro\n","3.sacar saldo\n","4.Salir\n")
saldo=1000
banco=input("Introduzcion una opcion del menu")

while banco!="4":
    if(banco=="1"):
        print(saldo)
    elif(banco=="2"):
            ingreso=int(input("INtroduzca la cantidad a ingresar")) 
            saldo=saldo+ingreso
    elif(banco=="3"):
         retirar=int(input("Itroduzca la cantidad a sacar")) 
         saldo=saldo-retirar
    print("1.Ver saldo \n","2.reintegro\n","3.sacar saldo\n","4.Salir\n")
    