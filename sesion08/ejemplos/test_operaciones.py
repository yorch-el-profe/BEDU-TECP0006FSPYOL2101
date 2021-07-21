from operaciones import *

def test_suma_cero():
  resultado = suma(0, 0)
  # Espero que resultado sea 0
  assert resultado == 0

def test_suma_numeros_iguales():
  assert suma(2, 2) == 2 * 2
  assert suma(8, 8) == 8 * 2
  assert suma(10000, 10000) == 10000 * 2

def test_suma_cadenas():
  resultado = suma("Hello ", "World")
  assert len(resultado) > 0
  assert type(resultado) == str
  assert resultado == "Hello World"