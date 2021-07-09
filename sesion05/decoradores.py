# En Python las funciones son de orden superior
# Son funciones que reciben funciones y regresan funciones

def funcion_a():
  print("Ejecutando funcion A")

def funcion_b(f):
  print("Ejecutando funcion B")
  f()

  def funcion_c():
    print("Ejecutando funcion C")

  return funcion_c

#g = funcion_b(funcion_a)
#g()

# Un decorador es una función se ejecuta PRIMERO que otra función
# El decorador TIENE que regresar una función que SUSTITUYE A LA ORIGINAL
def mi_primer_decorador(hello_world):
  print("Ejecutando mi primer decorador")

  def funcion_dummy():
    print("Esto es una funcion dummy")
    hello_world()

  # Este return SUSTITUYE LA IMPLEMENTACION de la funcion original
  return funcion_dummy

@mi_primer_decorador
def hello_world():
  print("Hello World")

hello_world()
