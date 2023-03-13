from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField, SelectField, TelField, TextAreaField, SubmitField)

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'miclavesecreta'


class Formmulario(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    edad = BooleanField('Eres mayor de edad')
    sexo = RadioField('Sexo:', choices=[
                      ('h', 'hombre'), ('m', 'mujer')])
    color = SelectField('Color favorito', choices=[
                        ('r', 'rojo'), ('v', 'verde'), ('a', 'azul')])

    comentario = TextAreaField()
    boton = SubmitField('Enviar')

# Definimos las rutas de nuestra aplicacion


@app.route('/informacion')
def informacion():
    return render_template('informacion.html')


@app.route('/datos', methods=['GET', 'POST'])
def datos():
    miformulario = Formmulario()
    # Validamos si el formulario ha sido enviado
    if miformulario.validate_on_submit():
        # Guardamos la informacion del usaurio en la session
        session['nombre'] = miformulario.nombre.data
        session['edad'] = miformulario.edad.data
        session['sexo'] = miformulario.sexo.data
        session['color'] = miformulario.color.data
        session['comentario'] = miformulario.comentario.data
        # Enviamos nuestros datos regogidos a otro template, en etse caso esta llamando a la funcion informacion que nos manda a informacion.html
        return redirect(url_for('informacion'))

    return render_template('datos.html', formulario=miformulario)

#Necesario para arrancar la app
if __name__=='__main__':
    app.run(debug=True)

