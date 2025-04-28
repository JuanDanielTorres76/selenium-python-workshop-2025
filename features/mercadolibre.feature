Feature: Search and verify products on MercadoLibre

  Scenario: Verify that searching "iPhone 13" shows results containing "iPhone"
    Given I am on the MercadoLibre home page
    When I search for the product "iPhone 13"
    Then I should see results containing the word "iPhone"
