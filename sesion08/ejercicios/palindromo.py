def es_palindromo(cadena):
  resultado = cadena.lower().replace(" ", "")
  return resultado == resultado[::-1]