cont=0
lista=[]

while cont != 10:
    dato=input("INTRODUZCA UNA ASIGNATURA: ")
    lista.append(dato)#si no pinemos el append no se añadira lo que ocurrira es que se remplazara no se puede pasar eso 
    cont += 1

print("--- TUS ASIGNATURAS ---")
for asignatura in lista:  # Recorremos la lista directamenta con este bucle 
    print(f"Mi asignatura es {asignatura}")
