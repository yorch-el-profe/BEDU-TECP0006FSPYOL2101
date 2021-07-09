def ignora_negativos(suma):
  def verdadera_implementacion(*numeritos):
    lista_filtrada = []

    for numero in numeritos:
      if numero > 0:
        lista_filtrada.append(numero)
    
    return suma(*lista_filtrada)
  return verdadera_implementacion

@ignora_negativos
def suma(*numeritos):
  total = 0
  for numero in numeritos:
    total = total + numero
  return total

print(suma(1,2,3,4,5,6,7,8,9,10, -100, -50, -20))