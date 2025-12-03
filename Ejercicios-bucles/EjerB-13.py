frase = input("Introduce una frase: ")
letra = input("Introduce una letra para buscar: ")

frecuencia = frase.lower().count(letra.lower())

print(f"La letra '{letra}' aparece {frecuencia} veces en la frase.")