from examples.calculos import suma, cuadrado

def cuadrado_binomio(a, b):
    """ Calculamos (a + b)^2 = a^2 + 2ab + b^2 usando suma y cuadrado(funciones que ya hicimos) """
    try:
        a2 = cuadrado(a)  
        b2 = cuadrado(b)  
        doble_ab = 2 * int(a) * int(b) 
        parte1 = suma(a2, b2)           
        return suma(parte1, doble_ab)   
    except (TypeError, ValueError):
        return None
