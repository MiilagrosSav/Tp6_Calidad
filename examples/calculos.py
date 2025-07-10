def suma(a, b):
    """ Realiza la suma de dos números.
    Convierte los argumentos a float. Si falla, devuelve None.
    """
    try:
        num_a = float(a)
        num_b = float(b)
        return num_a + num_b
    except (TypeError, ValueError):
        return None


def cuadrado(a):
    """ Calcula el cuadrado de un número.
    Convierte el argumento a float. Si falla, devuelve None.
    """
    try:
        num = float(a)
        return num * num
    except (TypeError, ValueError):
        return None
