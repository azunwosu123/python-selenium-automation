# Created by nazua at 4/11/2023
Feature: test cases for the cart page
  # Enter feature description here

  Scenario: User can search for a product on Amazon
    Given Open Amazon.com
    When Click on cart icon
    Then verify Sign in is opened: Sign in header is visible, email input field is present