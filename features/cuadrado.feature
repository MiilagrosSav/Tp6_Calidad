Feature: Cuadrado

  Scenario: Calcular el cuadrado de un número positivo
    Given tengo el número 4
    When calculo el cuadrado
    Then el resultado del cuadrado debe ser 16

  Scenario: Calcular el cuadrado de un número negativo
    Given tengo el número -3
    When calculo el cuadrado
    Then el resultado del cuadrado debe ser 9

  Scenario: Calcular el cuadrado de una cadena no numérica
    Given tengo el número hola
    When calculo el cuadrado
    Then el resultado del cuadrado debe ser None

  Scenario: Calcular el cuadrado de un valor nulo
    Given tengo el número None
    When calculo el cuadrado
    Then el resultado del cuadrado debe ser None

