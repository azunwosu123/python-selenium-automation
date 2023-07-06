# HW 4_2
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: Check the product in cart
    Given Open amazon main page
    When Search for Table
    When Add to Cart
    Then Verify that product is in the cart