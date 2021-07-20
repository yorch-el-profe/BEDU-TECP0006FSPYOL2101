from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
@app.route("/")
def index():
  # render_template "envia" un archivo html
  return render_template('index.html')

@app.route("/saluda/<nombre>")
def saluda(nombre):
  return render_template('saluda.html', persona=nombre)