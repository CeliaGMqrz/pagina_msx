from flask import Flask,render_template,abort, request
import json
app = Flask(__name__)

with open("MSX.json") as fichero:
    info=json.load(fichero)

@app.route('/')
def inicio():
	return render_template("inicio.html")

@app.route('/juegos',methods=["GET","POST"])
def juegos():
    return render_template("juegos.html")


@app.route('/listajuegos', methods=["POST"])
def listajuegos():
	cadena=request.form.get("name")
	juegos=[]
	desarrolladores=[]
	for juego in info:
		if cadena in str(juego["nombre"]):
			juegos.append(str(juego["nombre"]))
			desarrolladores.append(str(juego["desarrollador"]))
			filtro=zip(juegos,desarrolladores)	
		elif cadena == "":
			juegos.append(juego["nombre"])
	return render_template("listajuegos.html",juegos=filtro)

app.run(debug=True)

