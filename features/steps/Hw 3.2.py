from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click Orders')
def click_orders(context):
    context.driver.find_element(By.ID, "nav-orders").click()

@then('Verify Sign In page Opens')
def verify_signin_opens(context):
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert actual_result == 'Sign in', f'Expected Sign in header but got {actual_result}'
    # verify email field present
    context.driver.find_element(By.XPATH, "//input[@type='email']")