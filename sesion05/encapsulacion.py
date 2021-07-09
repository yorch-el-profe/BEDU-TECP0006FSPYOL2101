"""
# nombre, edad, vacunado son atributos públicos
class Persona:
  nombre = "Paquito"
  edad = 34
  vacunado = False

  def presentate(self):
    print("Hola me llamo", self.nombre)

paquito = Persona()

# Sobreescribiendo el valor del atributo "nombre"
paquito.nombre = "Juanito"

paquito.presentate()

"""

# Los atributos privados deben empezar con "__"
# Los atributos privados NO se heredan
"""
class CuentaBancaria:

  def __init__(self, abonoInicial):
    self.__monto = abonoInicial

  def abonar(self, abono):
    self.__monto = self.__monto + abono

  def estado_cuenta(self):
    print(self.__monto)

guardadito = CuentaBancaria(50)
guardadito.abonar(100)
"""

# Prohibido porque monto ahora es "PRIVADO"
# print(guardadito.monto)

# Esta creando una propiedad "nueva" (pública) llamada "__monto"
# que es diferente de la original (privada)
#guardadito.__monto = 200000

#print(guardadito.__monto)

# Correcto
#guardadito.abonar(100)
#guardadito.estado_cuenta()

# Los atributos protegidos (protected) pueden ser leidos y actualizados
# dentro de la misma clase y sus clases hijos, pero no desde afuera.
# Los atributos protegidos llevan un "_" en su nombre
# ESTO ES UNA CONVENCION
class CuentaBancaria:
  _monto = 0

  def __init__(self, abonoInicial):
    self._monto = abonoInicial

  def abonar(self, abono):
    self._monto = self._monto + abono

  def estado_cuenta(self):
    print(self._monto)

class CuentaPremium(CuentaBancaria):

  def __init__(self):
    super().__init__(10000)

  def estado_cuenta_premium(self):
    print("Usuario premium su estado de cuenta es:", self._monto)

premium = CuentaPremium()

#premium.estado_cuenta()
premium._monto = 200
premium.estado_cuenta_premium()

"""
Ejercicio: Diseñar una maquina expendedora de dulces

class MaquinaExpendedora:
  ...


maquina = MaquinaExpendedora()

maquina.comprar("A0") # -> "Chocolate"
maquina.comprar("B1") # -> "Coca Lata"

maquina.dulces # PROHIBIDO
maquina.dulces[0] # PROHIBIDO
"""