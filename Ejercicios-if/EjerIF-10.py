ingredientes_base = ["Mozzarella", "Tomate"]
ingredientes_vegetarianos = ["Pimiento", "Tofu"]
ingredientes_no_vegetarianos = ["Peperoni", "Jamón", "Salmón"]

print("Bienvenido a la pizzería Bella Napoli\n")

# Preguntar al usuario el tipo de pizza
decision = input("¿Deseas una pizza vegetariana? (Escribe S para Sí o N para No): ").upper()

tipo_pizza = ""
ingrediente_elegido = ""

# --- Rama Vegetariana ---
if decision == "S"or decision == "s":
    tipo_pizza = "vegetariana"
    # Mostramos el menú vegetariano manualmente, sin bucle
    print("\nIngredientes vegetarianos disponibles:\n1. Pimiento\n2. Tofu")
    
    # Pedir elección al usuario
    opcion_str = input("Elige un ingrediente (1 o 2): ")
    
    # Validar y asignar ingrediente usando if/elif, sin bucle
    if opcion_str == "1":
        ingrediente_elegido = ingredientes_vegetarianos[0]
    elif opcion_str == "2":
        ingrediente_elegido = ingredientes_vegetarianos[1]
    else:
        print("Opción no válida. Se añade Pimiento por defecto.")
        ingrediente_elegido = ingredientes_vegetarianos[0]

#Pra ver si no es vegetariana  
elif decision == "N"or decision == "n":
    tipo_pizza = "no vegetariana"
    # Mostramos el menú no vegetariano manualmente, sin bucle
    print("\nIngredientes no vegetarianos disponibles:\n1. Peperoni\n2. Jamón\n3. Salmón")
        
    # Pedir elección al usuario
    opcion_str = input("Elige un ingrediente (1, 2 o 3): ")
    
    # Validar y asignar ingrediente usando if/elif, sin bucle
    if opcion_str == "1":
        ingrediente_elegido = ingredientes_no_vegetarianos[0]
    elif opcion_str == "2":
        ingrediente_elegido = ingredientes_no_vegetarianos[1]
    elif opcion_str == "3":
        ingrediente_elegido = ingredientes_no_vegetarianos[2]
    else:
        print("Opción no válida. Se añade Peperoni por defecto.")
        ingrediente_elegido = ingredientes_no_vegetarianos[0]


else:
    print("Opción no válida. Por favor, introduce S o N.")
    tipo_pizza = None # Marcamos que la elección fue inválida

# --- Mostrar el pedido final ---
# Solo se ejecuta si la elección inicial (S/N) fue válida
if tipo_pizza:
    # Creamos la lista final de ingredientes
    ingredientes_finales = ingredientes_base + [ingrediente_elegido]
    
    print(f"\n--- Tu pedido ---")
    print(f"Pizza: {tipo_pizza.capitalize()}")
    # Usamos .join() para mostrar la lista de forma elegante, sin bucle
    print("Ingredientes:\n- " + "\n- ".join(ingredientes_finales))