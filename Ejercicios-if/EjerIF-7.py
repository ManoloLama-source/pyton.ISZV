Renta = int(input("Introduzca su la renta anual: "))
if Renta < 10000:
  print("Su tipo impositivo es del 5%")
elif Renta >= 10000 and Renta < 20000:
  print("Su tipo impositivo es del 15%")
elif Renta >= 20000 and Renta < 35000:
  print("Su tipo impositivo es del 20%")
elif Renta >= 35000 and Renta < 60000:
  print("Su tipo impositivo es del 30%")
else:   
  print("Su tipo impositivo es del 45%")