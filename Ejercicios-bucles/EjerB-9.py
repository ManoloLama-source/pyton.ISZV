contrasena_guardada = "python123"
contrasena_usuario = ""


while contrasena_usuario != contrasena_guardada:
    contrasena_usuario = input("Introduce la contraseña: ")
    
    if contrasena_usuario != contrasena_guardada:
        print("Contraseña incorrecta, intenta de nuevo.")

print("¡Bienvenido! Contraseña correcta.")