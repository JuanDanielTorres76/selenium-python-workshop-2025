Feature: Search and verify Wikipedia article title

  Scenario: Verify the title of the Python programming language article
    Given I am on the Wikipedia home page
    When I search for "Python (lenguaje de programación)"
    Then I should see the article title "Python (lenguaje de programación)"
