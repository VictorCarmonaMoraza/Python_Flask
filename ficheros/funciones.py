# Funciones

# Crear una funcion
def hola():
    print("Hola buenos dias")


# LLamada a la funcion
hola()


def sumar(numero1, numero2):
    resultado = numero1+numero2
    print(resultado)


sumar(5, 3)


def sumar2(numero1, numero2):
    resultado = numero1+numero2
    return resultado


suma = sumar2(5, 23)
print(suma)


# Verificadno tipos
def sumar3(numero1, numero2):
    """sumary_line
  Esta funcion suma dos numeros enteros
  Ejemplo de llamada:
    """
    if type(numero1) == type(numero2) == type(10):
        resultado = numero1+numero2
    else:
        resultado = "Error deben ser numeros"
    return resultado


sumar = sumar3(13, 456)
print(sumar)
