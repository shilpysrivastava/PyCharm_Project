Feature: Create a new booking

  @createbooking
  @pytest.mark.order(1)
  Scenario: Create a new booking by passing the booking details
    Given User has booking details
    When User send booking details
    Then response status code should be 200
    Then response should be json
    Then response should contain bookingid
