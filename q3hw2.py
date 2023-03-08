from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.maximize_window()

driver.get('https://www.amazon.com')

driver.find_element(By.ID, "nav-orders").click()

actual_result = driver.find_element(By.XPATH, '//h1[@class="a-spacing-small"]').text
expected_result = "Sign in"
assert actual_result == expected_result, f'Expected {expected_result} but got {actual_result}'

driver.find_element(By.XPATH, "//input[@id='ap_email']")

print('Test Passed')

driver.quit()
