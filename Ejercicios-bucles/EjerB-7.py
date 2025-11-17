
 # Bucle externo: controla qué tabla estamos haciendo (la del 1, la del 2, etc.)
for i in range(1, 11):
    # Imprimimos un título para cada tabla
    print(f"\nTabla del {i}")
    
    # Bucle interno (anidado)
    for j in range(1, 11):
        # Calculamos el resultado
        resultado = i * j
        # Imprimimos la operación
        print(f"{i} x {j} = {resultado}")


