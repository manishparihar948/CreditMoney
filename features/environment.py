from selenium import webdriver

def before_scenario(context, scenario):
    print("Chrome Driver Executed")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


def after_scenario(context, scenario):
    print("Chrome Driver Closed")
    context.driver.close()
