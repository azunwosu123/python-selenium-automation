# HW 4_2
from behave import *
from selenium.webdriver.common.by import By

TABLE_PAGE = (By.XPATH,"//span[@class='a-truncate-cut']")


@when ('Add to Cart')
def Add_to_Cart(context):
    context.driver.find_element(*TABLE_PAGE).Add()

@then('verify that product is in the cart')
def verify_product_in_the_cart(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH,"//span[@class='a-truncate-cut']").text
    assert expected_result == actual_result, f'Error! Expected {expected_result} bot got actual {actual_result}]'
