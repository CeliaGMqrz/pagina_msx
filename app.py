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
	identificadores=[]
	for juego in info:
		if cadena in str(juego["nombre"]):
			juegos.append(str(juego["nombre"]))
			desarrolladores.append(str(juego["desarrollador"]))
			identificadores.append(str(juego["id"]))
			filtro=zip(juegos,desarrolladores,identificadores)	
		elif cadena == "":
			juegos.append(juego["nombre"])
	return render_template("listajuegos.html",juegos=filtro)

@app.route('/juego/<int:identificador>', methods=["GET","POST"])
def detallejuego(identificador):
	juegos=[]
	desarrolladores=[]
	identificadores=[]
	sistemas=[]
	distribuidores=[]
	categorias=[]
	anyos=[]

	for juego in info:
		if identificador == int(juego["id"]):
			juegos.append(str(juego["nombre"]))
			desarrolladores.append(str(juego["desarrollador"]))
			identificadores.append(str(juego["id"]))
			sistemas.append(str(juego["sistema"]))
			distribuidores.append(str(juego["distribuidor"]))
			categorias.append(str(juego["categoria"]))
			anyos.append(str(juego["año"]))
			filtro=zip(identificadores,juegos,sistemas,distribuidores,desarrolladores,categorias,anyos)	
	return render_template("detallejuego.html",juegos=filtro)
		

app.run(debug=True)

