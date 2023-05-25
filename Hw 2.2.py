from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')


# Amazon Logo
driver.find_element(By.XPATH,"//i[@aria-label='Amazon']")

# Continue button
driver.find_element(By.XPATH,"//input[@id='continue']")

# Need help link
driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']")

# Forgot your password link
driver.find_element(By.XPATH, "//a[contains(text(), 'Forgot your password')]")

# Other issues with Sign-In link
driver.find_element(By.XPATH,"//a[@id='ap-other-signin-issues-link']")

# Create your Amazon account button
driver.find_element(By.XPATH,"//a[@id='createAccountSubmit']")

# Privacy Notice link
driver.find_element(By.XPATH,"//a[contains(text(), 'Privacy Notice')]")

# Conditions of Use
driver.find_element(By.XPATH, "//a[contains(text(), 'Conditions of Use')]")

