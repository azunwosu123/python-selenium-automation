from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


COLOR_OPTIONS = (By.XPATH,"//span[@class='a-button-inner']")
CURRENT_COLOR = (By.XPATH, "//span[@class='selection']")

@given('Open Amazon product {product_id} page')
def open_product_page(context, product_id):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')



@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['Black', 'Blue Over Dye', 'Dark Blue Vintage', 'Dark Indigo', 'Dark Wash', 'Indigo Wash', 'Light Blue Vintage', 'Light Wash', 'Medium Blue Vintage', 'Medium Wash', 'Rinsed', 'Vintage Wash', 'Washed Black', 'Bright White', 'Dark Khaki Brown', 'Light Khaki Brown', 'Olive']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS) # => [WebElement1, WebElement2, WebElement3]

    for color in colors[13:30]:
        # WebElement2
        color.click() # WebElement2.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [current_color]

    assert expected_colors == actual_colors, \
        f'Expected colors {expected_colors} did not match actual {actual_colors}'
