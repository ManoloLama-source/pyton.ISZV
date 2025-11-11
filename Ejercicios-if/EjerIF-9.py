edad =int(input("Introduce tu edad: "))
if edad<4:
    print("Tu entrada es gratuita")
elif edad>4 and edad<=18:
    print("Tu entrada cuesta 5€")
elif edad>18:
    print("Tu entrada cuesta 10€")