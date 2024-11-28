import time

from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class LoginPage(BasePage):
    username = (By.ID, 'urname')
    password = (By.ID, 'urpass')
    login_button = (By.XPATH, '//input[@value="ავტორიზაცია"]')

    def enter_username(self, username):
        self.send_keys(self.username, username)

    def enter_password(self, password):
        self.send_keys(self.password, password)

    def click_login(self):
        self.click(self.login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        time.sleep(1)

    def click_teachers_page(self):
        self.click((By.NAME, 'choose_admin'))
        time.sleep(1)

    def click_student_page(self):
        self.click((By.NAME, 'choose_student'))
        time.sleep(1)
