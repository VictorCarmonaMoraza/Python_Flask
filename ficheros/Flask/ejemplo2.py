from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def portada():
    return render_template("portada.html")

@app.route("/hola")
def hola():
    return render_template("hola.html")


if __name__ == '__main__':
    app.run(debug=True)
