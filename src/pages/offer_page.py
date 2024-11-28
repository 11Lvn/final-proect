import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.pages.base_page import BasePage

class OfferPage(BasePage):

    def create_multiple_offers(self, offers):
        for offer in offers:
            self.create_offer(offer['title'],
                              offer['type'],
                              offer['audience'],
                              offer['publish_date'],
                              offer['cancel_date'],
                              offer['text'],
                              offer['image'])

    def create_offer(self, offer_title, offer_type, offer_audience, offer_publish_date, offer_unpublish_date, offer_text,
                     offer_image):
        add_news_btn = self.driver.find_element(By.CLASS_NAME, 'news-add-btn')
        add_news_btn.click()
        time.sleep(2)
        title = self.driver.find_element(By.ID, 'title')
        title.send_keys(offer_title)
        type_ = Select(self.driver.find_element(By.ID, 'type'))
        type_.select_by_visible_text(offer_type)
        audience = Select(self.driver.find_element(By.ID, 'audience'))
        audience.select_by_visible_text(offer_audience)
        publish_date = self.driver.find_element(By.ID, 'publish_date')
        unpublish_date = self.driver.find_element(By.ID, 'unpublish_date')
        publish_date.send_keys(offer_publish_date)
        unpublish_date.send_keys(offer_unpublish_date)
        submit = self.driver.find_element(By.CLASS_NAME, 'form-submit-btn')
        text = self.driver.find_element(By.CLASS_NAME, 'ql-editor')
        text.send_keys(offer_text)

        self.driver.execute_script("arguments[0].scrollIntoView();", submit)
        submit.click()
        time.sleep(1)
