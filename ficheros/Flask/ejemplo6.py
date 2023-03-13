from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField


app = Flask(__name__)

app.config['SECRET_KEY'] = 'miclavesecreta'


# Creamos el formulario
class Formulario(FlaskForm):
    boton = SubmitField("Enviar mensaje")


# Generamos la ruta
@app.route("/mensaje", methods=['GET', 'POST'])
def mensaje():
    # Instanciamos las clase Formulario
    formulario = Formulario()

    # Verficamos si el formualrios se ha enviado
    if formulario.validate_on_submit():
        flash("Gracias por pulsar este boton")
        return redirect(url_for('mensaje'))
    return render_template('mensaje.html', formulario=formulario)


if __name__ == '__main__':
    app.run(debug=True)
