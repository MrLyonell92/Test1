#@title CineDuoc
import math

compra = 0
palomitas = 0
bebida = 0
estreno = 4800
normal = 2900
p_peq = 2500
p_med = 4500
p_gra = 7800
b_peq = 1000
b_med = 1250
b_gra = 2000

print("Hola y bienvenido al CineDuoc!\nSi el cliente pertenece a DuocUC favor solicitar credencial (Estudiante o Funcionario).\n¿El cliente pertenece a Duoc? [si]/[no] ")

opcion = input("\nIngrese opción: ")
if (opcion == "si"):
  print("El cliente pertenece a DuocUC")
  opcion = True
else:
  print("El cliente no pertenece a DuocUC")

print("\n¿Qué tipo de entrada desea?\n[1]/[2]\n1. Estreno $4800\n2. Normal $2900")

entrada = input("Ingrese opción: ")
if (entrada == "1"):
  compra = estreno
  print("Ha seleccionado Estreno")
elif (entrada == "2"):
  compra = normal
  print("Ha seleccionado Normal")

if (opcion == True):
  compra = round(compra *0.7)
else:
  compra = compra

print("\n¿Desea agregar palomitas a su pedido?\n[si]/[no]")
opcion = input("Ingrese opción: ")
if (opcion == "si"):
  print("\nQué tamaño de palomitas quiere?\n[1]/[2]/[3]\n1. Palomitas pequeñas $2500\n2. Palomitas medianas $4500\n3. Palomitas grandes $7800")
  palomitas = input("Ingrese opcion: ")
  if (palomitas == "1"):
    palomitas = p_peq
    print("Se ha agregado una palomita pequeña")
  elif (palomitas == "2"):
    palomitas = p_med
    print("Se ha agregado una palomita mediana")
  elif (palomitas == "3"):
    palomitas = p_gra
    print("Se ha agregado una palomita grande")
  else: 
    palomitas = 0

else:
  print("No se agregó palomitas")

print("\n¿Desea agregar bebida a su pedido?\n[si]/[no]")
opcion = input("Ingrese opción: ")
if (opcion == "si"):
  print("\nQué tamaño de bebida quiere?\n[1]/[2]/[3]\n1. Bebida pequeña $1000\n2. Bebida mediana $1250\n3. Bebida grande $2000")
  bebida = input("Ingrese opcion: ")
  if (bebida == "1"):
    bebida = b_peq
    print("Se ha agregado una bebida pequeña")
  elif (bebida == "2"):
    bebida = b_med
    print("Se ha agregado una bebida mediana")
  elif (bebida == "3"):
    bebida = b_gra
    print("Se ha agregado una bebida grande")
  else: 
    bebida = 0

else:
  print("No se agregó bebida")

compra = compra + palomitas + bebida
print(f"\nEl total a pagar es ${compra}")
efectivo = int(input("\nFavor indicar efectivo ingresado: "))
if (efectivo > compra):
  vuelto = efectivo - compra
  print(f"Su vuelto es de ${vuelto}")
  print("\n¡Que disfrute su función!")
elif (efectivo == compra):
  print("No requiere vuelto ya que ha pagado justo")
  print("\n¡Que disfrute su función!")
elif (efectivo < compra):
  faltante = compra - efectivo
  print(f"Le falta dinero para cancelar el total, le falta la cantidad de ${faltante}")
