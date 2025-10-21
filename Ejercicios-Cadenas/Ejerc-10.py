# Pedir los productos separados por comas
productos = input("Ingresa los productos de la cesta de compra, separados por comas: ")

# Dividir los productos
lista_productos = productos.split(',')

# Mostrar cada producto reemplazando comas por saltos de línea
print("\nTu cesta de compra contiene:") 
print('\n'.join(lista_productos))#Al hacer \n havc que la lista se ponga en lines nuevas 
#y el join lo que hace es unir las cosas en este caso la lista se "une" por lineas nuevas