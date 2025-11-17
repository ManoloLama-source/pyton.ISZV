a =int(input("Dime un numero del 1 al diez opar hace cuenta atras "))

cuaneta_a=[]
#volvemos a crear una lista para almacenar los ddatos


for i in range(a, -1 ,-1): #si ponemos el menos 1 el vcero se añade si ponemos el cero se queda en 1 
    cuaneta_a.append(str(i))


resultado =",".join(cuaneta_a)

print (resultado)