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

# Ejercicio 5
def num5(valor_auto, dev, inc_terreno):
  if valor_auto*dev < inc_terreno/2:
    print("Compro el auto")
  else:
    print("No compro el auto")
  print("######################################################")  

# Ejercicio 6
def num6(unit):
  total = unit*11000
  if unit < 5:
    print("Descuento: "+ str(total*0.1))
  elif unit >= 5:
    print("Descuento: "+ str(total*0.2))
  elif unit >= 10:
    print("Descuento: "+ str(total*0.4))
  print("######################################################")  

# Ejercicio 7
def num7(price,marca):
  if marca=="NOSY" & price >= 2000:
    desc = price*0.15
  else:
    if price >= 2000:
      desc = price*0.1
  tot = price - desc
  print("Total a pagar: "+tot)    
  print("######################################################") 

# Ejercicio 8
def num8(total):
  if total>500000:
    inv=total*0.55
    prest=total*0.3
    cred=total*0.15
  else:
    inv=total*0.7
    prest=0
    cred=total*0.3
  inter=cred*0.2
  print("Cantidad a Invertir: "+str(inv))
  print("Cantidad a Prestamo: "+str(prest))  
  print("Cantidad a Credito: "+str(cred))  
  print("Cantidad de Intereses: "+str(inter))    
  print("######################################################") 

# Ejercicio 9
def num9(a,b):
  if a==b:
    print("Multiplicación: "+str(a*b))
  elif a>b:
    print("Multiplicación: "+str(a-b))
  else:  
    print("Multiplicación: "+str(a+b))
  print("######################################################")   