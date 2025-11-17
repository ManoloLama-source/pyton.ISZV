numero = int(input("Pon un numeor entero positivo: "))

numero_imp=[]
#creamos una lista para almacenar los datos 


for i in range(1, numero+1,2): 
    #Le etamos diciendo que empice en unoy que llege hasta el numero indicado(numero+1)y que hag saltos de dos en dos
    
    numero_imp.append(str(i))#Convertimos lo nuimero en un stringpara ponerlo en una lista


resultado = ",".join(numero_imp) 

print(resultado)
