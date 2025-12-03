euros=int(input("Introduzca una cantidad de euros"))

e10 = 10
e5 = 5
e2 = 2
e1 = 1

t10 = 0
t5 = 0
t2 = 0
t1 = 0

while euros >= e10:
    t10 = euros // e10 
    euros =  euros % e10

while euros >= e5:
    t5 = euros // e5
    euros = euros % e5

while euros >= e2:
    t2 = euros // e2
    euros = euros % e2

while euros >= e1:
    t1 = euros // e1
    euros = euros % e1

total = t10+ t5 + t2 + t1

print(f"total de monedas es {total}")
print(f"Se han usado {t10} de 10,{t5} de 5,{t2} de dos y {t1} de 1")