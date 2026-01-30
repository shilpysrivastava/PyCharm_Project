Feature: Authentication Token
  @skip
  Scenario: Generate auth token successfully
    Given Valid username and password
    When User send request with valid username and password
    Then response status code should be 200
     And response should be json
    And auth token generate successfully
