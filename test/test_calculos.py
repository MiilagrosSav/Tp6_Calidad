import pytest
from examples.calculos import suma, cuadrado

@pytest.mark.parametrize("a, b, esperado", [
    (2, 3, 5),
    (2, -3, -1),
    (0, 5, 5),
    (None, 5, None),
    (2, None, None),
    ('2', '3', 5),
    (1.5, 2.5, 4.0),
    (2, suma(2, 2), 6)
])
def test_suma(a, b, esperado):
    assert suma(a, b) == esperado

@pytest.mark.parametrize("n, esperado", [
    (4, 16),
    (-3, 9),
    (0, 0),
    ('5', 25),
    (None, None),
    ('abc', None)
])
def test_cuadrado(n, esperado):
    assert cuadrado(n) == esperado
