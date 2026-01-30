Feature: Get booking details by ID
  @fetchbookingdetails
  @pytest.mark.order(2)
  Scenario: Fetch booking details
    Given booking service is available
    When I fetch booking details for created booking
    Then response should be json
    And response status code should be 200
    And print all the booking details for created booking

