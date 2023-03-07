# Conjuntos en python

conjunto = set()
print(conjunto)


# Añadir elementos a un conjunto
conjunto.add(1)
conjunto.add(2)
conjunto.add(3)
conjunto.add('Hola')
print(conjunto)

# Borrar elementos de un conjunto
conjunto.discard('Hola')
conjunto.discard(2)
print(conjunto)

# En los conjuntos los elementos que sonm iguales solo se añaden una vez
# Lo intentamos varias veces pero como vemos no admite valores repetidos y solo acepta uno
conjunto.add(25)
conjunto.add(25)
conjunto.add(25)
conjunto.add(25)
conjunto.add(25)
print(conjunto)

#Convertimos una lista de elementos repetidos a un conjunto para eliminar los repetidos
lista = [1, 2, 2, 2, 2, 2, 3, 6, 3, 3, 3, 3, 3, 44, 4, 4, 6]
conjunto2 = set(lista)
print(conjunto2)
