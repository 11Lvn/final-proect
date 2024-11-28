from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def send_keys(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.send_keys(text)

    def click(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    def check_item(self, class_name, title, check_exists):
        items = self.driver.find_elements(By.CLASS_NAME, class_name)
        if check_exists:
            for item in items:
                if item.text == title:
                    return True
            else:
                return False
        else:
            for item in items:
                if item.text == title:
                    return False
            else:
                return True
