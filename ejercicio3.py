#@title Venta de Zapatos

zapato = 20000

print("Hola y bienvenido a Shoe's'Shop\nA modo de promoción si compras 2 pares o más, el envio es GRATIS!\nDe lo contrario debe pagar $3000 de envio")
cantidad = int(input("\nSeleccione la cantidad de pares de zapatos a comprar: "))
if (cantidad >= 2):
  total = cantidad * zapato
  print(f"\nEl total a pagar es ${total}")
else: 
  total = (cantidad * zapato) + 3000
  print(f"\nEl total a pagar es ${total}")  
