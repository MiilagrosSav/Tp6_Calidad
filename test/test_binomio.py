from examples.binomio import cuadrado_binomio

def test_binomio():
    assert cuadrado_binomio(2, 3) == 25
    assert cuadrado_binomio('1', '2') == 9
    assert cuadrado_binomio(None, 3) == None
    assert cuadrado_binomio('a', 1) == None
