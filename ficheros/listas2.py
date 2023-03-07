lista = [1, 2, "verde", 5, "antonio"]
print(lista)


# Elimina el ultimo elemento de la lista pop
lista.pop()
print(lista)

# Eliminar el primer elemento de la lista lista.pop(index)
lista.pop(0)
print(lista)

# Darle la vuelta de una lista
lista2 = [1, 2, "verde", 5, "antonio"]
lista2.reverse()
print(lista2)

# Ordena lista
listaNumerica = [5, 9, 23, 1, 16, 3, 7]
listaNumerica.sort()
print(listaNumerica)

# Listas anidadas es una lista dentro de otra lista
listaAnidadas = [1, 2, 3, 4, ['rojo', 'verde']]
print(listaAnidadas)

# Accedo al color verde de la listas anidadas
accesoElementoRojo = listaAnidadas[4][0]
print(accesoElementoRojo)

# crear una lista a partir de otra lista
#Coje los primeros elementos de cada lista y crea una lista nueva
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista_nueva = [elemento[0] for elemento in matriz]
print(lista_nueva)
