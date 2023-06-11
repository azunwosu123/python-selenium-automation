from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click cart icon')
def click_cart_icon (context):
    context.driver.find_element(By.XPATH, "//div[@id='nav-cart-container']").click()

@then('Verify Cart is empty')
def verify_Cart_empty(context):
    actual_result = context.driver.find_element(By.XPATH,'//div[@class="a-row sc-your-amazon-cart-is-empty"]/h2' ).text
    assert actual_result == 'Your Amazon Cart is empty', f'Expected Sign in header but got {actual_result}'
    # verify email field present
    context.driver.find_element(By.XPATH, "//input[@type='email']")