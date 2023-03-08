from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def portada():
    return render_template("portada.html")


@app.route("/hola")
def hola():
    diccionario = {'nombre': 'Antonio', 'edad': '35', 'color': 'verde'}
    return render_template("hola.html", datos=diccionario)


@app.route("/colores")
def colores():
    lista_colores = ["verde","rojo", "amarillo", "azul"]
    return render_template("colores.html", colores = lista_colores)


if __name__ == '__main__':
    app.run(debug=True)
