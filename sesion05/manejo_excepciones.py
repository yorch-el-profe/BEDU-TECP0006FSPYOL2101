# Errores lanzados en tiempo de ejecución
# TypeError: Se intenta operar con tipos diferentes
# NameError: No existen variables
# ZeroDivisionError: Se intentó dividir entre 0 
# ValueError: Intento transformar un valor erroneo
# RecursiveError

# Exception: Un error genérico

# raise: Lanza un error creado desde programación (manualmente)
#raise Exception("Algo malo paso aquí")

from fibo_decoradores import fibo

print("Ingresa un número para la secuencia fibo")
secuencia = input()

try: #Ejecutar código potencialmente peligroso (puede provocar un error)
  resultado = fibo(int(secuencia))
  print("El resultado es", resultado)
except ValueError: # Bloque exclusivo para errores de tipo ValueError
  print("Error: Ingresaste un valor que no es un número")
except Exception as e: # Bloque genérico (atrapa cualquier error)
  print(e)