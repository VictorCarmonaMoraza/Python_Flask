from flask import Flask

app = Flask(__name__)


@app.route("/")
def principal():
    return "<h1>Hola,buenos dias</h1>"

@app.route("/adios")
def adios():
    return "<h2>Adios, hasta la proxima</adios>"

#rutas dinamicas
@app.route("/saludar/<nombre>")
def saludar(nombre):
    return "<h2>La letra en la posicion 5 del nombre es {}".format(nombre[5])

@app.route("/longitud/<nombre>")
def longitud(nombre):
    valor = len(nombre)
    return "<h2>La longitud de la cadena {} tiene {} letras".format(nombre,valor)


#Arreglar errores

if __name__ == '__main__':
    app.run()
