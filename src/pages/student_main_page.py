import time

from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class StudentMainPage(BasePage):

    def click_offers(self):
        element = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/nav/ul/li[12]/a/div[2]')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        element.click()
        time.sleep(1)
