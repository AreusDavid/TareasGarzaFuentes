# Librería no utilizada


def factorial(num):

    # Verificar que num sea un entero positivo
    if not (isinstance(num, int) and not isinstance(num, bool) and num >= 0):
        return -50, None

    # Condición para finalizar la recursividad
    elif num == 0:
        resultado = 1

    # La función se llama a si misma
    else:
        resultado = num * factorial(num-1)[1]

    return 0, resultado
