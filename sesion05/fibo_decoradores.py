import time

"""
  La secuencia de fibonacci es la siguiente:

  1 1 2 3 5 8 13 21 34 55 89 ...

  fibonacci(x) = fibonacci(x - 1) + fibonacci(x - 2)
  si x es 1 o 2 entonces el resultado es 1

  fibonacci(5) = fibonacci(4) + fibonacci(3)
  (izquierdo) fibonacci(4) = fibonacci(3) + fibonacci(2)
  (izquierdo) fibonacci(3) = fibonacci(2) + fibonacci(1) = 1 + 1 = 2

  Por lo tanto
  fibonacci(4) = 2 + 1 = 3

  Por lo tanto
  fibonacci(5) = 3 + fibonacci(3)

  (derecho) fibonacci(3) = fibonacci(2) + fibonacci(1) = 1 + 1 = 2

  Por lo tanto

  fibonacci(5) = 3 + 2 = 5

  Por lo tanto el resultado es 5
"""
def memoize(f):
  memoria = {}
  
  def wrapper(x):
    if x not in memoria:
      memoria[x] = f(x)
    return memoria[x]
  return wrapper

@memoize
def fibo(x):
  if x <= 0:
    raise Exception("Fibonacci solo acepta números positivos")

  if x == 1 or x == 2:
    return 1

  return fibo(x - 1) + fibo(x - 2)

#start_time = time.time() # Tomando el tiempo inicial

#print(fibo(-1))

#end_time = time.time() # Tomando el tiempo final

#print("el algoritmo tardo {} segundos".format((end_time - start_time)))