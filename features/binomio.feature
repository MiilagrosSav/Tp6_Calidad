Feature: Cuadrado del binomio

  Scenario: Calcular el cuadrado del binomio (1 + 2)
    Given tengo los valores del binomio 1 y 2
    When calculo el cuadrado del binomio
    Then el resultado debe ser 9