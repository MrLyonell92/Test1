#@title Convertidor de divisas

clp = 1
dl_aus = 539
p_arg = 4
yen = 6

print("Bienvenido al convertidor de divisas extranjeras a pesos chilenos\nPor favor seleccione la divisa que desea convertir: [1]/[2]/[3]\n1. Dólar Australiano\n2. Peso Argentino\n3. Yen Japones")
opcion = input("Ingrese opción: ")
if (opcion == "1"):
  print("\nUd ha selecionado Dólar Australiano\n¿Qué desea hacer? [1]/[2]\n1. De Dólar Australiano a Peso Chileno\n2. De Peso Chileno a Dólar Australiano")
  opcion1 = input("Ingrese opción: ")
  if (opcion1 == "1" ):
    opcion2 = int(input("\nIngrese cantidad de Dólar Australiano a convertir: $"))
    conversion = dl_aus * opcion2 
    print(f"Son ${conversion} pesos.")
  elif (opcion1 == "2" ):
    opcion2 = int(input("\nIngrese cantidad de Peso Chileno a convertir: $"))
    conversion = round(opcion2/dl_aus, 2) 
    print(f"Son ${conversion} dólares.")
elif (opcion == "2"):
  print("\nUd ha selecionado Peso Argentino\n¿Qué desea hacer? [1]/[2]\n1. De Peso Argentino a Peso Chileno\n2. De Peso Chileno a Peso Argentino")
  opcion1 = input("Ingrese opción: ")
  if (opcion1 == "1" ):
    opcion2 = int(input("\nIngrese cantidad de Peso Argentino a convertir: $"))
    conversion = p_arg * opcion2 
    print(f"Son ${conversion} pesos Chilenos.")
  elif (opcion1 == "2" ):
    opcion2 = int(input("\nIngrese cantidad de Peso Chileno a convertir: $"))
    conversion = round(opcion2/p_arg, 2) 
    print(f"Son ${conversion} pesos Argentinos.")
elif (opcion == "3"):
  print("\nUd ha selecionado Yen Japonés\n¿Qué desea hacer? [1]/[2]\n1. De Yen Japonés a Peso Chileno\n2. De Peso Chileno a Yen Japonés")
  opcion1 = input("Ingrese opción: ")
  if (opcion1 == "1" ):
    opcion2 = int(input("\nIngrese cantidad de Yen Japonés a convertir: $"))
    conversion = yen * opcion2 
    print(f"Son ${conversion} pesos.")
  elif (opcion1 == "2" ):
    opcion2 = int(input("\nIngrese cantidad de Peso Chileno a convertir: $"))
    conversion = round(opcion2/yen, 2) 
    print(f"Son ${conversion} yenes.")
