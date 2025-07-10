Feature: Cuadrado del binomio

  Scenario: Calcular el cuadrado del binomio (1 + 2)
    Given tengo los valores del binomio 1 y 2
    When calculo el cuadrado del binomio
    Then el resultado del binomio debe ser 9

  Scenario: Calcular el binomio con texto inválido
    Given tengo los valores del binomio hola y 2
    When calculo el cuadrado del binomio
    Then el resultado del binomio debe ser None

  Scenario: Calcular el binomio con None y número
    Given tengo los valores del binomio None y 5
    When calculo el cuadrado del binomio
    Then el resultado del binomio debe ser None

  Scenario: Calcular el binomio con ambos valores None
    Given tengo los valores del binomio None y None
    When calculo el cuadrado del binomio
    Then el resultado del binomio debe ser None
