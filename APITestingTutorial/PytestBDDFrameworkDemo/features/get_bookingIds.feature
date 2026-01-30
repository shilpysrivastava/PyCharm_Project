Feature: Get all booking IDs

  @skip
  Scenario: Retrieve all booking IDs without filters
    Given booking service is available
    When I send a get request
    Then response should be json
    And response status code should be 200
    And response should not be empty
    And response should contain booking ids

