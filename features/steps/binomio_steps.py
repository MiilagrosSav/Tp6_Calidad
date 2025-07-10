from behave import given, when, then
from examples.binomio import cuadrado_binomio

@given("tengo los valores del binomio {a} y {b}")
def step_given_numeros(context, a, b):
    try:
        context.a = None if a == "None" else float(a)
    except ValueError:
        context.a = None
    try:
        context.b = None if b == "None" else float(b)
    except ValueError:
        context.b = None

@when("calculo el cuadrado del binomio")
def step_when_binomio(context):
    context.resultado = cuadrado_binomio(context.a, context.b)

@then("el resultado del binomio debe ser {esperado}")
def step_then_resultado(context, esperado):
    esperado_val = None if esperado == "None" else float(esperado)
    assert context.resultado == esperado_val
