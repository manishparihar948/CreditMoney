from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Logs import logs_file

log = logs_file.get_logs()

class SeleniumHelper:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, page_url):
        self.driver.get(page_url)

    def click(self, locator):
        self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).click()

    def send_keys(self, locator):
        self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).send_keys()

    def insert_text_in_input_field(self, locator, input_text):
        self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).send_keys(input_text)

    def wait_till_element_is_present(self, locator, timeout=10):
        flag = False
        try:
            log.info(f"Waiting {timeout} seconds for element {list(locator.values())[0]} presence")
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((list(locator.keys())[0], list(locator.values())[0])))
            log.info(f"Element found")
            flag = True
        except Exception as e:
            log.error(
                f"Element {list(locator.values())[0]} not found after waiting {timeout} seconds")
        return flag