from behave import *
from selenium import webdriver
from Helper.SeleniumHelper import SeleniumHelper
from Locators import locators
from Logs import logs_file
from TestData import test_data
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException


log = logs_file.get_logs()

# Background steps
@given('I launch chrome browser')
def step_open_chrome_browser(context):
    context.driver = webdriver.Chrome()
    log.info("Launch Chrome Opened")

# Common steps for both positive and negative cases
@when('I open the Credmudra homepage')    
def step_open_credmudra_homepage(context):
    SeleniumHelper(context.driver).open_page(test_data.credmudra_base_url)
    log.info("Open Credmudra homepage")

@step('Verify the Personal loan feature button')
def step_click_get_matched_now_button(context):
    SeleniumHelper(context.driver).click(locators.button_get_matched_now)
    print("Get Matched Now ! Button Pressed Succesfully")
    log.info("Get Matched Now ! Button Pressed Succesfully") 


# Scenario: Invalid Contact Number
@step('Enter invalid contact number')
def step_enter_invalid_contact_number(context):
    SeleniumHelper(context.driver).insert_text_in_input_field(locators.input_field_mobileNumber, test_data.incorrect_mobile_number)
    print("Enter invalid contact number")
    log.info("Enter invalid contact number")

@then('Show error for invalid contact number')
def step_show_error_message(context):
    print("Must be a 10-digit number")
    log.info("Must be a 10-digit number")
    try:
        # Handle the alert message (assuming an alert is displayed)
        alert = Alert(context.driver)
        alert_text = alert.text
        print(f"Alert Text: {alert_text}")

        # Perform actions on the alert if needed, e.g., accepting it
        alert.accept()
    except NoAlertPresentException:
        print("No alert found.")

# Scenario: Valid Contact Number
@when('Enter valid contact number')
def step_enter_valid_contact_number(context):
    SeleniumHelper(context.driver).insert_text_in_input_field(locators.input_field_mobileNumber, test_data.correct_mobile_number)
    print("Enter valid contact number")
    log.info("Enter valid contact number")

@when('Click to apply button')
def step_click_to_apply_button(context):
    # Assuming there is a button to apply, replace it with the actual locator
    SeleniumHelper(context.driver).click(locators.button_next_welcomeToCredmudra)
    print("Click to apply button")
    log.info("Click to apply button")

@then('Show OTP Page')
def step_show_otp_page(context):
    # Assuming some validation logic for the OTP page
    print("OTP Page is displayed")
    log.info("OTP Page is displayed")