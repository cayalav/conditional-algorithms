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

# Ejercicio 3
def num3(monto):
  if monto < 50000:
    monto=monto*0.03
    print("Total de descuento: "+str(monto))
  else:
    monto=monto*0.02
    print("Total cuota a pagar: "+str(monto)) 
  print("######################################################")  

# Ejercicio 4
def num4(prom, dias_adicionales, gan_diarias, dias_prod_detenida):
  if dias_prod_detenida:
    perdida = gan_diarias*7
    print("Total de perdida: "+str(perdida))
  else  :
    if (prom > 170):
      perdida = (gan_diarias*0.5*dias_adicionales)
      print("Total de perdida: "+str(perdida))
    else:
      print("No hay multa ni sanción")
  print("######################################################") 