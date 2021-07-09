class Moneda:
  def __init__(self, valor = 1):
    self.valor = valor

  # Ayuda a dar un "formato" o una interpretación en texto de un objeto
  def __str__(self):
    return "${}".format(self.valor)

# Agregación: Reutilizar objetos dentro de otros objetos

class Monedero:

  def __init__(self):
    self.monedas = []

  def __str__(self):
    return "Hola soy un monedero"

  # Accion (metodo)
  def agregar_moneda(self, valor):
    self.monedas.append(Moneda(valor))
  
  def monto_total(self):
    total = 0
    for moneda in self.monedas:
      total = total + moneda.valor
    return total

monederito = Monedero()

monederito.agregar_moneda(10)
monederito.agregar_moneda(5)
monederito.agregar_moneda(20)

print(monederito)
print(monederito.monto_total())

"""
  Ejercicio: Implementar un codigo que simule un carrito de compra.

  carrito.agregar_producto(producto)
  carrito.agregar_producto(producto)
  carrito.agregar_producto(producto)

  carrito.monto_total() // $1,000
"""