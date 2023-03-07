class Persona():
    def __init__(self, nombre):
        texto = ''
        self.nombre = nombre

    def saludar(self):
        self.texto = "Hola, mi nombre es "+self.nombre
        return self.texto


# Instanciamos un objeto der la clase persona
persona1 = Persona("Antonio")
print(type(persona1))
print(persona1.nombre)
texto = persona1.saludar()
print(texto)

# Herencia


class Adulto(Persona):
    def __init__(self, nombre):
        Persona.__init__(self, nombre)


# Creamos uhn objeto ASdulto
adulto1 = Adulto("Antonio")
print(type(adulto1))

texto2 = adulto1.saludar()
print(texto2)
