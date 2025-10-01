Dinero=float(input("¿Cuanto dinero tienes en la cuenta?: "))

interes= 0.04
año=1
while año <= 3:
    beneficios=Dinero*(1+interes)
    print(f"El dinero que has obtenido en el año {año} es de {beneficios} euros")
    año+=1 
    #Con lo ultimo le hemos dicho que sume 1 hasta que llegue a 3 años ya que asi se lo hemos dicho en el while 

