"""
  Las clases son una plantilla que describe a un objeto (entidad, modelo, cosa)
"""
# pascal case -> cada palabra la inicio con mayuscula
# AnitaLavaLaTina
class MiPrimerClase:
  pass

"""
  Los objetos son "instancias" de una clase.

  Instancia -> Referencia de memoria.
"""
# camel case -> la primera es minuscula, cada palabra la inicio con mayuscula
# anitaLavaLaTina
miPrimerObjecto = MiPrimerClase()

# print(miPrimerObjecto)

class Moneda1:
  # atributos (propiedades)
  valor = 1

class Moneda2:
  valor = 2

class Moneda5:
  valor = 5

class Moneda10:
  valor = 10

class Moneda20:
  valor = 20

#moneda1 = Moneda1()

# Notación punto: Acceder atributos o métodos  ( objeto.algo )
#print(moneda1.valor)

class Moneda:
  """
    El constructor de una clase es una función especial
    que se ejecuta SIEMPRE al momento de crear
    una instancia del objeto.
  """
  def __init__(self, valor = 1, color = "Plata"):
    print("Ejecutando el constructor de la clase Moneda")
    self.valor = valor # Creando el atributo "valor" con valor 10
    self.color = color

moneda10 = Moneda(10, "Oro")
moneda5 = Moneda(5, "Plata")

moneda1 = Moneda()

print(moneda10.valor)
print(moneda10.color)
print(moneda5.color)