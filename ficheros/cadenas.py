texto = "Hola, buenos dias"
print(texto)

#Acceder a posiciones de un caracter
caracter = texto[0]
print(caracter)

#El ultimo caracter se obtendria como:
ultimoCaracter = texto[-1]
print(ultimoCaracter)

#Obtner la data de la posicion 0 a la 3
#Debemos poner hasta la cuerta porque el siempre quita la ultima poscion
textoHola = texto[0:4]
print(textoHola)

#Obtener buenos dias del texto
textoBuenosDias = texto[6:]
print(textoBuenosDias)

#Obtener texto de 2 en dos, se salta las segunda poscion
textoBuenosDias2 = texto[6::2]
print(textoBuenosDias2)

#Establece toda la cadena en mayuscula
mayusculas = texto.upper()
print(mayusculas)

#Establece toda la cadena en minuscula
minusculas = texto.lower()
print(minusculas)

#Separar la cadena de colores
colores = "rojo,verde,azul,negro"
listaColores = colores.split(",")
print(listaColores)

#Obtener colores por la posicion de la lista anterior
Primercolor = listaColores[0]
print(Primercolor)