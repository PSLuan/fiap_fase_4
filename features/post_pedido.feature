Feature: POST pedido endpoint

  Scenario: Posting a pedido
    Given a pedido payload
    When the pedido is posted to the endpoint
    Then the response status code should be 200
    And the response should contain the posted pedido data

  Scenario Outline: Posting a pedido with invalid data
    Given an invalid pedido payload with <invalid_field>
    When the invalid pedido is posted to the endpoint
    Then the response status code should be 400
    And the response should contain an error message