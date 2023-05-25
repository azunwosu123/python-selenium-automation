from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# init driver
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()

driver.get('https://www.amazon.com/')

# By xpath
driver.find_element(By.ID, "nav-orders").click()

expected_result = "Sign in"
actual_result = driver.find_element (By.XPATH,"//h1[@class='a-spacing-small']").text
assert expected_result == actual_result

print('Test case passed')


email = driver.find_element (By.XPATH,"//input[@type='email']")
assert email.is_displayed(), f"Email field is not present"
print('Test case passed')