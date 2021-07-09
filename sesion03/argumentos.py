# Definición de la función
def mi_primer_funcion():
  print("Hola mundo")


# args
# keywords args
def saluda(*nombres, simbolo = "!"):
  print(type(nombres)) # <class 'tuple'>

  for nombre in nombres:
    print("Hola", nombre, simbolo, sep = "_")


# Invoco a la función
# mi_primer_funcion()

#saluda("Fernando", "Jorge", "Aurelio", "Uriel", "Juan", simbolo = "*")

"""
  Ejercicio 01. Escribir una función que reciba
  una cantidad indeterminada de números y regrese
  la suma de todos ellos.
"""

# ------------------------------------------------------------------

#print("Juan", "Pablo", "Pepito", "Maria", "Javier", sep = " - ")

"""
  Ejercicio 02. Escribir una función que reciba
  una cantidad indeterminada de números y un parámetro
  adicional para especificar la operación (+, -, *).

  math(1,2,3,4,5,6,7,8,9 op = "-")
  1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9

  tuple[0]
"""

# kwargs
def describe_persona(**persona):
  print(type(persona)) # <class 'dict'>

  for key, value in persona.items(): # [("nombre","Paquito"), ("edad", 30), ... ]
    print(key, value)

describe_persona(nombre = "Paquito", edad =  30, direccion = "Calz Guadalupe #1340") 