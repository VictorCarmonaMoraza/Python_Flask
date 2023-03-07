

lista = [1, 2, 3]
print(lista)


# las listas en python pueden ser de cualquier tipo
lista2= ['antonio', 'luis', 2, 40, 'maria', 1, 4, 25]
print(lista2)

#Primer elemento de una lista
elemento = lista2[0]
print(elemento)

#Ultimo elemento de una lista
ultimoElemento = lista2[-1]
print(ultimoElemento)

#Elementos de una poscion a otra
#Obtenemos los elementos de la poscion 1 a la 3
elementosIntermedios = lista2[1:3]
print(elementosIntermedios)

#Añadir adatos a la lista por el final
nuevosElementos = ['rojo','verde','azul','amarillo']
lista2.append(nuevosElementos)
print(lista2)

#Aqui concatena los elementos uno detras de otro aunque le agreguemos una lista
lista3= ['antonio', 'luis', 2, 40, 'maria', 1, 4, 25]
nuevosElementos2 = ['rojo','verde','azul','amarillo']
lista3.extend(nuevosElementos2)
print(lista3)

elemento = lista2[8]
print(elemento)

elemento1 = lista3[8]
print(elemento1)