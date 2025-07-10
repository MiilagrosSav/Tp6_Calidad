from behave import given, when, then
from examples.calculos import cuadrado

@given("tengo el número {a}")
def step_given_num(context, a):
    try:
        context.a = None if a == "None" else float(a)
    except ValueError:
        context.a = None

@when("calculo el cuadrado")
def step_when_cuadrado(context):
    context.resultado = cuadrado(context.a)

@then("el resultado del cuadrado debe ser {esperado}")
def step_then_resultado(context, esperado):
    esperado_val = None if esperado == "None" else float(esperado)
    assert context.resultado == esperado_val
