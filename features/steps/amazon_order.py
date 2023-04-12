from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Amazon.com')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Orders')
def click_on_order(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


# @then('verify Sign in is opened: Sign in header is visible, email input field is present')
# def verify_SignIn_Page (context):
#     actual_text = context.driver.find_element(By.XPATH,"//span[@class='nav-action-inner']").text
#     expected_text = 'verify Sign in page opened'
#     assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'


@then('verify Sign in is opened: Sign in header is visible, email input field is present')
def verify_Sign_header (context):
    sleep(2)
    actual_text = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    expected_text = 'Sign in'
    assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'
    email_field = context.driver.find_element(By.ID, 'ap_email')
    assert email_field, f'Expected email field not found'


def verify_email_input (context):
    actual_text = context.driver.find_element(By.XPATH,"//input[@type='email']").text
    expected_text =  'email Input field is present'
    assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'