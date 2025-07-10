from behave import given, when, then
from examples.calculos import suma

@given("tengo los números {a} y {b}")
def step_given_numeros(context, a, b):
    try:
        context.a = None if a == "None" else float(a)
    except ValueError:
        context.a = None
    try:
        context.b = None if b == "None" else float(b)
    except ValueError:
        context.b = None

@when("los sumo")
def step_when_sumo(context):
    context.resultado = suma(context.a, context.b)

@then("el resultado debe ser {esperado}")
def step_then_resultado(context, esperado):
    esperado_val = None if esperado == "None" else float(esperado)
    assert context.resultado == esperado_val
