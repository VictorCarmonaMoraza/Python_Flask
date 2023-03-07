from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def portada():
    return render_template("portada.html")

@app.route("/hola")
def hola():
    valor ="Antonio"
    valor_edad = "35"
    return render_template("hola.html", nombre =valor,edad=valor_edad)


if __name__ == '__main__':
    app.run(debug=True)
