import pytest

from src.pages.student_main_page import StudentMainPage
from src.pages.login_page import LoginPage
from src.pages.offer_page import OfferPage
from src.pages.teacher_main_page import AdminMainPage
from src.test.config import get_config, get_offers_config
from src.test.driver import get_driver


@pytest.fixture
def setup():
    config = get_config()
    driver = get_driver(config['browser'])
    driver.get(config['base_url'])
    yield driver
    driver.quit()


@pytest.fixture
def offers_config():
    config = get_offers_config()
    return config


@pytest.mark.usefixtures("setup", "offers_config")
def test_login_and_create_offers(setup, offers_config):
    config = get_config()
    admin_user = config['admin_user']

    driver = setup

    login_page = LoginPage(driver)
    login_page.login(admin_user['email'], admin_user['password'])
    login_page.click_teachers_page()
    teacher_main_page = AdminMainPage(driver)
    teacher_main_page.click_offers()

    offer_page = OfferPage(driver)
    offer_page.create_multiple_offers(offers_config)
    assert True


@pytest.mark.usefixtures("setup", "offers_config")
def test_student_page(setup, offers_config):
    config = get_config()
    student_user = config['student_user']

    driver = setup

    login_page = LoginPage(driver)
    login_page.login(student_user['email'], student_user['password'])
    # login_page.click_student_page()
    student_main_page = StudentMainPage(driver)
    student_main_page.click_offers()
    assert student_main_page.check_item(class_name='sales-item-text', title=offers_config[0]['text'], check_exists=True)
    assert student_main_page.check_item(class_name='sales-item-text', title=offers_config[1]['text'], check_exists=False)

@pytest.mark.usefixtures("setup", "offers_config")
def test_admin_page(setup, offers_config):
    config = get_config()
    admin_user = config['admin_user']

    driver = setup

    login_page = LoginPage(driver)
    login_page.login(admin_user['email'], admin_user['password'])
    login_page.click_teachers_page()
    admin_main_page = AdminMainPage(driver)
    admin_main_page.click_offers()
    admin_main_page.get_offers_and_check([o['title'] for o in offers_config])
    assert admin_main_page.check_item(class_name='table-news-title', title=offers_config[0]['title'], check_exists=True)
    assert admin_main_page.check_item(class_name='table-news-title', title=offers_config[1]['title'], check_exists=True)
