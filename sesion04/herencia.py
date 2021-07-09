class Carrito:

  def __init__(self):
    self.canasta = []

class Refresco:
  def __init__(self, nombre, precio, sabor, etiquetas):
    self.precio = precio
    self.nombre = nombre
    self.sabor = sabor
    self.etiquetas = etiquetas

class Helado:
  def __init__(self, nombre, precio, sabor, presentacion, etiquetas):
    self.precio = precio
    self.nombre = nombre
    self.sabor = sabor
    self.presentacion = presentacion
    self.etiquetas = etiquetas

class Tortillas:
  def __init__(self, nombre, precio, cantidad, etiquetas):
    self.nombre = nombre
    self.precio = precio
    self.cantidad = cantidad
    self.etiquetas = etiquetas

Refresco("Coca Cola", 15, "Cola", 4)
Refresco("Peñafiel", 10, "Agua Mineral", 0)

Helado("Vienetta", 87, "Vainilla", "Pastel", 3)
Helado("Mordisco", 17, "Vainilla con Chocolate", "Galleta", 3)

Tortillas("Tortillinas", 20, 12, 1)
Tortillas("Mateo", 18, 30, 0)