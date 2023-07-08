from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


AMAZON_PRIVACY_NOTICE =(By.XPATH,"//a[contains(text(), 'Privacy Notice')]")

@given('Open Amazon T&C page')
def open_TC_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 ')

@when('Store original windows')
def store_original_windows(context):
    context.original_window = context.driver.window_handles[0]
    print('Original:', context.original_window)
    print ('All windows:', context.driver.window_handles)

@when('Click on Amazon Privacy Notice link')
def Click_image(context):
    context.driver.find_element(*AMAZON_PRIVACY_NOTICE).click()


@when('Switch to the newly opened window')
def switch_newly_Opened_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    all_windows = context.driver.window_handles
    print('After window opened, all windows:', all_windows)
    context.driver.switch_to.window(all_windows[-1])


@then('Verify Amazon Privacy Notice page is opened')
def Verify_Privacy_Notice_page_Opened(context):
    context.driver.wait.until(EC.url_contains("/help/customer/"))

@then('User can close new window')
def Verify_close_new_windows(context):
    context.driver.close()
    all_windows = context.driver.window_handles
    print('After closed new window, all windows,all_windows')
@then('Switch back to original')
def switch_back_to_original(context):
     context.driver.switch_to.window(context.original_window)
     context.driver.wait.until(EC.new_window_is_opened)


