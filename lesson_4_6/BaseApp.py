import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
from datetime import datetime
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://localhost/litecart/"

    def find_element(self, locator, wait_time=10):
        return WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, wait_time=10):
        return WebDriverWait(self.driver, wait_time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self, site=""):
        return self.driver.get(self.base_url + site)

    def go_to_link(self, site):
        return self.driver.get(site)

    def screenshot(self, name='none'):
        ts = int(time.time())
        path_screen = os.getcwd() + f'\\screen\\{ts}_{name}.png'
        self.driver.save_screenshot(path_screen)

    def is_sorted(self, lst, key=lambda x: x):
        for i, el in enumerate(lst[1:]):
            # Проверка идет в str.lower(), чтобы регистр не влиял на сортировку
            if key(el).lower() < key(lst[i]).lower():  # i is the index of the previous element
                return [key(el), key(lst[i])]
        return True

    def input_text(self, elem, text):
        input_elem = self.find_element(elem)
        input_elem.clear()
        input_elem.send_keys(text)

    def scroll_to_elem(self, elem):
        actions = ActionChains(self.driver)
        actions.move_to_element(elem).perform()

    def wait_text_present_in_element(self, elem, text, wait_time=4):
        wait = WebDriverWait(self.driver, wait_time)
        wait.until(EC.text_to_be_present_in_element(elem, str(text)))

    def wait_open_new_win(self, current, wait_time=20):
        wait = WebDriverWait(self.driver, wait_time)
        wait.until(EC.new_window_is_opened(current))

    def get_log_type(self):
        print(self.driver.log_types)
        return self.driver.log_types

    def get_log_for_log_type(self, type_log):
        for logs in self.driver.get_log(type_log):
            print(logs)
