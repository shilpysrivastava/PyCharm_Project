Feature: Updates all current booking details
  Scenario: Update current booking
    Given booking service is available
    When Send bookingid with updated value
    Then response status code should be 200
    And response should be json
    And response should print updated value