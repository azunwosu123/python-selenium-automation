from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.maximize_window()

driver.get('https://www.amazon.com')

driver.find_element(By.ID, 'nav-orders').click()

driver.find_element(By.XPATH, '//h1[@class="a-spacing-small"]')

driver.find_element(By.ID, "createAccountSubmit")

driver.find_element(By.XPATH, "//input[@id='ap_email']")

driver.find_element(By.ID, 'ap_email')

driver.find_element(By.XPATH, "//input[@type='password']")

driver.find_element(By.XPATH, '//div[@class=a-alert-content"]')

driver.find_element(By.ID, "ap_password_check" )

driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")

driver.find_element(By.XPATH, "//a[contains(@href, '/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use']")

driver.find_element(By.XPATH,"//a[contains(@href, '/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice')]")

driver.find_element(By.XPATH, '//a[@class="a-link-emphasis"]')
