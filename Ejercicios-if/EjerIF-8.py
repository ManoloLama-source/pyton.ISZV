usuario1 = float(input("Introduce un número(0.0,0.4,0.6): "))
if usuario1 == 0.0:
    
    print("Usted tiene un nivel de rendimiento del 0.0 y cobrará 2400€")
elif usuario1==0.4:
    bonus1 = float(2400*usuario1)
    print (f"Usted tiene un nivel de rendimiento del 0.40.6 y cobrará {bonus1}€") 

elif usuario1==0.6 or usuario1>0.6:
    bonus2 = float(2400*usuario1)
    print (f"Usted tiene un nivel de rendimiento del 0.6 y cobrará {bonus2}€")  