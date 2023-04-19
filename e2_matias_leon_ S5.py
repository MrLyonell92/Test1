Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
Patente = []
Marca = []
Modelo = []
Año = []
Tipo = []
Registro = []

menuPrincipal = 0

while menuPrincipal != 4:

  try:
    menuPrincipal = int(input("Hola y bienvenido a ServiExpress \n\n Menú Principal: \n 1.- Registrar Automóvil \n 2.- Registrar Mantenimiento \n 3.- Consultar Automóvil \n 4.- Salir \n\n"))
  except ValueError:
    print("Por favor, ingrese un número válido.\n")
    continue
  
  if menuPrincipal == 1:
    print("Para regitrar un automóvil por favor llena los siguientes datos: \n")
    Patente.append(input("Patente [AA1000 o BBBB10]: "))
    Año.append(int(input("Año de fabricación [1900 a 2023]: ")))
...     Tipo.append(input("Tipo de vehículo \n d = diésel \n b = bencina \n e = eléctrico \n h = híbrido \n: "))
...     Marca.append(input("Marca vehículo [campo obligatorio]: "))
...     Modelo.append(input("Modelo vehículo [campo obligatorio]: "))
... 
...     print("Auto Registrado!")
... 
... 
...   elif menuPrincipal == 2:
...     print("Para registrar un mantenimiento por favor indique patente. \n")
...     cod = input("Ingresa patente: ")
...     for i in range(len(Patente)-1,-1,-1):
...       if Patente[i] == cod:
...           print("Patente registrada en nuestro sistema \n")
...           Registro.append(input("Registre mantenimiento: "))
...       else:
...         print("Patente no registrada en el sistema")
... 
...     
...   elif menuPrincipal == 3:
...     print("Para consultar un automovil por favor indique patente. \n")
...     cod = input("Ingresa patente a consultar: ")
...     for x in range(len(Patente)-1,-1,-1):
...       try: 
...         if Patente[x] == cod:
...           print("Patente   | Año de Fabricación | Tipo Vehículo | Marca    | Modelo      | Mantenimiento               \n")
...           print(Patente[x],"           ",Año[x],"              ",Tipo[x],"        ",Marca[x],"      ",Modelo[x],"    ",Registro[x])
...         else:
...           print("\nPatente consultada no esta en los registros")
...       except:
...         print(Patente[x],"           ",Año[x],"              ",Tipo[x],"        ",Marca[x],"      ",Modelo[x],"    ","Sin Registro")
... 
...   elif menuPrincipal == 4:
...     print("Cerrando sesión")
... 
...   else :
