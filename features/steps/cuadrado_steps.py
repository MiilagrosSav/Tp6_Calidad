from behave import given, when, then
from examples.calculos import cuadrado

@given("tengo el número {a}")
def step_given_num(context, a):
    context.a = float(a)

@when("calculo el cuadrado")
def step_when_cuadrado(context):
    context.resultado = cuadrado(context.a)

@then("el resultado debe ser {esperado:g}")
def step_then_resultado(context, esperado):
    assert context.resultado == esperado
