from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon.com')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on cart icon')
def click_on_cart(context):
    context.driver.find_element(By.ID, 'nav-cart-count').click()


@then('verify Amazon cart is empty')
def verify_cart_is_empty(context):
    actual_text = context.driver.find_element(By.XPATH, '//div[@class="a-row sc-your-amazon-cart-is-empty"]/h2').text
    expected_text = 'Your Amazon Cart is empty'
    assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'
