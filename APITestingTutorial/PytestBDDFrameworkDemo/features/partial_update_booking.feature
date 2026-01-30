Feature: Updates a current booking with a partially
  Scenario: Update current booking
    Given booking service is available
    When Send bookingid with updated value
    Then response status code should be 200
    Then response should be json
    Then response should print updated value


