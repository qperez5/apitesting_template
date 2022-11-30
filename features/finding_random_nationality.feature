Feature: Finding a random nationality

  Scenario Outline: Getting address

    Given a nationality <nat>
    When I call randomme API
    Then the response status code should be 200
    And the response header Content-Type should be application/json
    And the email address should be valid
    And the email has an arrow

    #And I should have an address from the country of the nationality
    #response = requests.get('https://api.github.com')

    Examples:
      | nat  |
      | CA   |
      | SS   |
      | EN   |
      | UK   |
      | SP   |
