import sys
import csv

codigo_postal = sys.argv[1]

resultados = []

with open("archivos/codigos_postales_cdmx.csv", "r") as archivo:
  reader = csv.reader(archivo)

  for linea in reader:
    if linea[0] == codigo_postal:
      resultados.append(linea[1])

print(resultados)