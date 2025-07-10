from behave import given, when, then
from examples.calculos import suma

@given("tengo los números {a} y {b}")
def step_given_numeros(context, a, b):
    context.a = float(a)
    context.b = float(b)

@when("los sumo")
def step_when_sumo(context):
    context.resultado = suma(context.a, context.b)

@then("el resultado debe ser {esperado:g}")
def step_then_resultado(context, esperado):
    assert context.resultado == esperado
