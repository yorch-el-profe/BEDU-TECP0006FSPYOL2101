print("Ingresa un numero:")
n = input()

num = int(n)

# IMPORTANTE: PYTHON ES UN LENGUAJE >>>>>>>> IDENTADO <<<<<<<<<

if num < 0:
  print("El numero es negativo")

  #if otra_condicion:
  #  linea
  #  linea
  #  linea
elif num > 0:
  print("El numero es positivo")
#elif num == 0:
else:
  print("El numero es cero")


print("Termino mi programa")