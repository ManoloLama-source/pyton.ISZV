dic= {'Euro':'€','Dollar':'$', 'Yen':'¥'}
pregunta=input("Di una divisa: ").capitalize
if pregunta in dic:
    print(dic[pregunta])
else:
    print(f'La moneda que ha introducido no es validad ')
    