from re import search

pattern = "lava"
text = "anita lava la tina"

result = search(pattern, text)

print("""
  El patron "{}" dentro del texto "{}"
  comienza a partir del indice {}
  y termina en el indice {}
""".format(pattern, text, result.start(), result.end()))