Feature: interfacing with a SatNav System

  Scenario: Searching for an address within a postcode
    Given that a user is on the search page
    When the user types a valid post code
    When the user clicks search
    Then a list of addresses within that post code should be displayed

  Scenario: Navigating to an address
    Given that a user has selected an address
    When the user selects Navigate
    Then the SatNav should display a route to the address

  Scenario: pull up list of addresses visited
    Given that a user is on the home page
    When the user selects History
    Then a list of last 10 addresses visited should be displayed
