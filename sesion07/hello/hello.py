from flask import Flask, request

# Crear una aplicación de Flask
app = Flask(__name__)

# Creando la ruta / (raíz/index/ruta principal)
@app.route("/")
def hello():
  return "Hello World"

@app.route("/suma")
def suma():
  # Acceder a un parámetro en Querystring
  # request.args.get('parametro', valor por defecto, tipo)
  param1 = request.args.get('a', 0, int)
  param2 = request.args.get('b', 0, int)
  resultado = param1 + param2
  return "La suma de {} + {} = {}".format(param1, param2, resultado)

@app.route("/saluda/<nombre>")
@app.route("/saluda/<nombre>/<int:edad>")
def saluda(nombre, edad = 18):
  print(type(edad))
  return "Hola, {} de {} años".format(nombre, edad)
