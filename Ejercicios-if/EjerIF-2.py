contraseña_guardada = "Juan1234"
contraseña_introducida = input("Introduce la contraseña: ")

if contraseña_introducida.lower == contraseña_guardada.lower:#los pone en minuscula y los compara 
                                                            #por eso es el .lower al final
    print("Las contraseñas coinciden.")

else:
    print("Las contraseñas no coinciden.")