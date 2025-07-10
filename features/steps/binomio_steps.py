from behave import given, when, then
from examples.binomio import cuadrado_binomio

@given("tengo los valores del binomio {a} y {b}")
def step_given_numeros(context, a, b):
    context.a = float(a)
    context.b = float(b)

@when("calculo el cuadrado del binomio")
def step_when_binomio(context):
    context.resultado = cuadrado_binomio(context.a, context.b)

@then("el resultado debe ser {esperado:g}")
def step_then_resultado(context, esperado):
    assert context.resultado == esperado 
