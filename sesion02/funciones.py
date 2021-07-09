# DRY (Don't Repeat Yourself)

# Definición de una función
def mi_primer_funcion():
  print("Mi primer funcion :)")

# "Llamar" o "Invocar" la función
mi_primer_funcion()

# Las funciones reciben parámetros (variables)
def saluda(nombre):
  print("Hola, {}".format(nombre))

saluda("Jorge")

def suma(numero1, numero2):
  return numero1 + numero2
  #resultado = numero1 + numero2
  #return resultado

print("1 + 2 = {}".format(suma(1,2)))
print("'abc' + 'edf' = {}".format(suma("abc", "edf")))
print("(1,2) + (3,4) = {}".format(suma((1,2), (3,4))))


"""
  Ejercicio 1. Crear una función que reciba como parámetro
  una lista de números y regresar la suma de todos sus elementos.

  sum_all([1,2,3,4,5]) -> 15
"""

def sum_all(list):
  result = 0
  for number in list:
    result = result + number
  return result

print("sum_all([1,2,3,4,5])", sum_all([1,2,3,4,5]))

"""
  Ejercicio 02. Fizzbuzz

  Crear una funcion llamada "fizzbuzz" que reciba como parámetro
  una lista de enteros positivos y que calcule lo siguiente:

  Por cada elemento N de la lista:

    * Si N es divisible entre 3, poner en pantalla "Fizz"
    * Si N es divisible entre 5, poner en pantalla "Buzz"
    * Si N es divisible entre 3 y 5, poner en pantalla "FizzBuzz"
    * Si N no es divisible entre 3 o 5, poner en pantalla el número

  fizzbuzz([1,2,3,4,5,15])

  1
  2
  Fizz
  4
  Buzz
  FizzBuzz

  Tip: Módulo (%)
"""

def fizzbuzz(lista):
  for i in lista:
    if i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(i)

fizzbuzz([1,2,3,4,5,15])

"""
  Ejercicio 03. Crear las siguientes funciones:

  Los humanos tienen 10 bases
  Los marcianos atacan 1 base a la vez
  Las bases no pueden ser atacadas mas de una vez

  attack(3) -> Destruir la base 3
  attack(5) -> Destruir la base 5
  game_over() -> False, quedan las bases 1 2 4 6 7 8 9 10
  attack(1)
  attack(2)
  attack(10)
  attack(8)
  game_over() -> False, quedan las bases 4 6 7 9
  attack(4)
  attack(6)
  attack(7)
  attack(9)
  game_over() -> True

  El objetivo es implementar dichas funciones


  Por último:

  attack(3.5) -> Atacaria la mitad de la base 3
  attack(4.2) -> Atacando el 20% de la base 4 y queda el 80%
  attack(4.6) -> Atacando el 60% de la base 4 y queda el 20%
  attack(4.2) -> Destruyo la base 4
  attack(5) -> Destruye al 100% la base 5
"""