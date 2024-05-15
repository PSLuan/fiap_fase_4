Feature: Pedido API

  Scenario: Get pedidos
    Given the pedido table has some data
    When I request the list of pedidos
    Then the response status code should be 200
    And the response should contain a list of pedidos