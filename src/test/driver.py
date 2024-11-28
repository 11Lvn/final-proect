from selenium import webdriver


def get_driver(browser_name):
    if browser_name == 'chrome':
        driver = webdriver.Chrome()
    else:
        raise ValueError(f'only Chrome allowed this time!')
    driver.maximize_window()
    return driver
