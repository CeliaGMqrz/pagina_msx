from flask import Flask,render_template,abort
import json
app = Flask(__name__)

with open("MSX.json") as fichero:
    info=json.load(fichero)

@app.route('/')
def inicio():
	return render_template("inicio.html")

@app.route('/juegos')
def juegos():
    return render_template("juegos.html")

app.run(debug=True)