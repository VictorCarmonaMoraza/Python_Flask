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
    return "<h2>Hola {}, byenos dias</h2>".format(nombre)



if __name__ == '__main__':
    app.run()
