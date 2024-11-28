import time

from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class AdminMainPage(BasePage):

    def click_offers(self):
        element = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/nav/ul/li[18]/a/div[2]')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        element.click()
        time.sleep(1)

    def get_offers_and_check(self, offer_names):
        elements = self.driver.find_elements(By.CLASS_NAME, 'table-news-title')
        for name in offer_names:
            for elem in elements:
                if elem.text == name:
                    parent_ = elem.find_element(By.XPATH, '..')
                    publ_date = parent_.find_element(By.CLASS_NAME, 'table-news-publish-date')
                    unpubl_date = parent_.find_element(By.CLASS_NAME, 'table-news-endate')
                    if publ_date.text >= unpubl_date.text:
                        return False
                    break
        return True

