#Ejercicios Taller Condicional - Carlos Ayala

# Ejercicio 1
def num1(n,total):
  if n > 3:
    total=total*0.7
    print("Total a pagar: "+str(total))
  else:
    total=total*0.9
    print("Total a pagar: "+str(total)) 
  print("######################################################") 

  # Ejercicio 2
def num2(random, total):
  if random < 74:
    total=total*0.15
    print("Total de descuento: "+str(total))
  else:
    total=total*0.2
    print("Total de descuento: "+str(total)) 
  print("######################################################")  