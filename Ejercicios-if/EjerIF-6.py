
# Solicitar y limpiar el nombre
nombre = input("Introduce tu nombre (solo la primera palabra): ")
sexo = input("Introduce tu sexo ('M' para Mujer, 'H' para Hombre): ")
   
    
    # Comprobar la primera letra del nombre
primera_letra = nombre[0]
    
    
if (sexo == 'M' and primera_letra < 'M') or \
(sexo == 'H' and primera_letra > 'N'):
        
        grupo = 'A'
        
    
else:
    grupo = 'B'
