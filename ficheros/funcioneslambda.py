# Funciones Lambda

lista = [1, 2, 3, 4, 5, 6]


def par(numero):
    resultado = (numero % 2) == 0
    return resultado


filtro = filter(par, lista)
pares = list(filtro)
print("No funcion lambda ",pares)



filtro2=filter(lambda numero:(numero % 2)==0,lista)
pares2=list(filtro2)
print("funcion lambda: ",pares2)