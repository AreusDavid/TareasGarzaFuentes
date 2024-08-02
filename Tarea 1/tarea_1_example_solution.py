def operation_selector(num1, num2, op):
    # Definir los códigos de error
    error_numero_invalido = -50
    error_no_string = -60
    error_operador_invalido = -70
    exito = 0

    # Verificar si num1 y num2 son enteros
    # ademas que no sean booleanos, ya que confunde booleanos con 1 y 0
    if not all(isinstance(x, int) and not isinstance(x, bool) for
               x in (num1, num2)):
        return error_numero_invalido, None

    # Verificar si op es un string
    if not isinstance(op, str):
        return error_no_string, None

    # Verificar si op es uno de los operadores
    if op not in ['+', '-', '*', '&']:
        return error_operador_invalido, None

    # Realizar la operación según el valor de op
    if op == '+':
        resultado = num1 + num2
    elif op == '-':
        resultado = num1 - num2
    elif op == '*':
        resultado = num1 * num2
    elif op == '&':
        resultado = num1 & num2

    # Devolver el resultado con código de éxito
    return exito, resultado


def calculo_promedio(lista_valores):
    # Verificar si la lista tiene más de 10 elementos
    if len(lista_valores) > 10:
        return -90, None  # Código de error 1: Lista demasiado grande

    # Verificar si todos los valores en la lista son números
    for i in lista_valores:
        if (not isinstance(i, (int, float)) or isinstance(i, bool)):
            # Código de error 2: No todos los valores son números
            # tambien revisa caso de bool
            return -80, None

    # Calcular el promedio si todas las validaciones son exitosas
    promedio = sum(lista_valores) / len(lista_valores)
    return 0, promedio  # Código de éxito 0
