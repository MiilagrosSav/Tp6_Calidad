Feature: Suma

  Scenario: Sumar dos enteros
    Given tengo los números 2 y 3
    When los sumo
    Then el resultado debe ser 5

  Scenario: Sumar un número y una cadena
    Given tengo los números 2 y hola
    When los sumo
    Then el resultado debe ser None

  Scenario: Sumar dos None
    Given tengo los números None y None
    When los sumo
    Then el resultado debe ser None

  Scenario: Sumar número válido y None
    Given tengo los números 4 y None
    When los sumo
    Then el resultado debe ser None
