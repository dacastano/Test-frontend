@regression_tests
Feature: Validate Navigation on the Menu Options from Home Page

  Background: 
    Given I navigate to the kayak main page
    Then I should be in the "home" page

  Scenario Outline: Navigate to the options on the Menu
    When I click on the "menu" "button"
    And I click on the "<option_name>" "option"
    Then I should be in the "<option_name>" page

    Examples:
      | option_name |
      | flights     |
      | stays       |