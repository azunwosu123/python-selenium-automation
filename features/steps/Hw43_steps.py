from behave import *
from selenium.webdriver.common.by import By

CUSTOMER_SERVICE_UI = (By.XPATH,By.XPATH, "//a[contains(text(), 'Customer Service']")
@given('Open amazon costumer page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@then('Verify these UI elements are present of the page')
def verify_UI_elements_Present(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//a[contains(text(), 'Customer Service']").text
    assert expected_result == actual_result, f'Error! Expected {expected_result} bot got actual {actual_result}]'
