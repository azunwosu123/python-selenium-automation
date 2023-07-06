# HW 4_1
from behave import *
from selenium.webdriver.common.by import By

BESTSELLER_PAGE = (By.CSS_SELECTOR,'#zg_header a')


@given("Open Amazon Bestseller page")
def step_impl(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('verify there are 5 links on the page')
def verify_link_count(context):
    links_count = len(context.driver.find_elements(*BESTSELLER_PAGE)) #5
    print(context.driver.find_elements(*BESTSELLER_PAGE))
    assert links_count == 5, f'Expected 5 links, bot got actual {links_count}]'