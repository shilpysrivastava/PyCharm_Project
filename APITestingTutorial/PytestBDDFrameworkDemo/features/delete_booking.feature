Feature: Delete booking
  Scenario: delete a booking from API
    Given bookingid is available
    When send bookingid
    Then response code should be 201
    And response contain text created