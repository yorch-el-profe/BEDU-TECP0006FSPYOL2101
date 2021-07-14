"""
archivo = open("archivos/hello_world.txt", "r")

# Leo una línea
print(archivo.readline())

# IMPORTANTE: Cerrar el archivo
archivo.close()
"""

# Modo w: Sobre escribe todo el archivo
with open("archivos/hello_world.txt", "w") as archivo:
  archivo.writelines(["Linea 1\n", "Linea 2\n", "Linea 3"])

# Modo r: Solo lectura
with open("archivos/hello_world.txt", "r") as archivo:
  for linea in archivo:
    print(linea)

# Modo a: Agrega nuevas lineas
with open("archivos/hello_world.txt", "a") as archivo:
  archivo.write("\nPython")