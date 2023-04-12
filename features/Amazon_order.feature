# Created by nazua at 4/11/2023
Feature: test case for the Orders page
  # Enter feature description here

  Scenario:User can search for a product on Amazon
     Given Open Amazon.com
    When Click on Orders
    Then verify Sign in is opened: Sign in header is visible, email input field is present