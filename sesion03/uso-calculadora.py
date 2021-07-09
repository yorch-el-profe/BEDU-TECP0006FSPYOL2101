# importar archivos o funciones

# 1. Importando todas las funciones de un archivo
# import modulo as alias
import calculadora

print(calculadora.suma(1, 2))
print(calculadora.resta(2,4))
print(calculadora.multiplicacion(5,4))

# 2. Importando una o varias funciones en específico
# from modulo import f1, f2, f3, ..., fn

from calculadora import division, multiplicacion

print(division(4,0))
print(multiplicacion(5, 4))

# 3. Importando todas las funciones de un archivo
# sin especificar una por una
# from modulo import *

from calculadora import *

print(modulo(2,4))