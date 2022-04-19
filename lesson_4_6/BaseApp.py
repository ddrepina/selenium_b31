from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://localhost/litecart/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self, site=""):
        return self.driver.get(self.base_url + site)

    def get_screen(self, name='none'):
        ts = datetime.now()
        print(f'{ts}_{name}')
        self.driver.save_screenshot(f'screen\\{ts}_{name}.png')
