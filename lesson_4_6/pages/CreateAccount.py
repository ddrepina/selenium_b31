import time

from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random


class CreateAccountLocators:
    LOCATOR_TAX_ID = (By.NAME, 'tax_id')
    LOCATOR_COMPANY = (By.NAME, 'company')
    LOCATOR_FIRST_NAME = (By.NAME, 'firstname')
    LOCATOR_LAST_NAME = (By.NAME, 'lastname')
    LOCATOR_ADDRESS = (By.NAME, 'address1')
    LOCATOR_POST_CODE = (By.NAME, 'postcode')
    LOCATOR_CITY = (By.NAME, 'city')
    LOCATOR_EMAIL = (By.NAME, 'email')
    LOCATOR_PHONE = (By.NAME, 'phone')
    LOCATOR_PASS = (By.NAME, 'password')
    LOCATOR_CONFIRMPASS = (By.NAME, 'confirmed_password')

    LOCATOR_COUNTRY_DROPDOWN_MENU = (By.CSS_SELECTOR, '[role="presentation"]')
    LOCATOR_COUNTY_INPUT = (By.CSS_SELECTOR, '[class="select2-search__field"]')
    LOCATOR_US = (By.XPATH, '//li[contains(text(), "United States")]')
    LOCATOR_SELECT_STATES = (By.CSS_SELECTOR, 'select[name = "zone_code"]')

    LOCATOR_BTN_CREATE_ACCOUNT = (By.NAME, 'create_account')

    LOCATOR_LOGOUT = (By.XPATH, '//li/a[contains(text(), "Logout")]')

    LOCATOR_BTN_LOGIN = (By.CSS_SELECTOR, 'button[name="login"]')


class CreateAccountHelper(BasePage):
    locators = CreateAccountLocators()

    def input_fname(self, fname):
        self.input_text(self.locators.LOCATOR_FIRST_NAME, fname)

    def input_lname(self, lname):
        self.input_text(self.locators.LOCATOR_LAST_NAME, lname)

    def input_address(self, address):
        self.input_text(self.locators.LOCATOR_ADDRESS, address)

    def input_postcode(self, postcode):
        self.input_text(self.locators.LOCATOR_POST_CODE, postcode)

    def input_city(self, city):
        self.input_text(self.locators.LOCATOR_CITY, city)

    def input_email(self, email):
        self.input_text(self.locators.LOCATOR_EMAIL, email)

    def input_phone(self, phone):
        self.input_text(self.locators.LOCATOR_PHONE, phone)

    def input_pass(self, password):
        self.input_text(self.locators.LOCATOR_PASS, password)

    def input_confirm_pass(self, password):
        self.input_text(self.locators.LOCATOR_CONFIRMPASS, password)

    def click_create_account(self):
        self.find_element(self.locators.LOCATOR_BTN_CREATE_ACCOUNT).click()

    def select_country(self, country):
        self.find_element(self.locators.LOCATOR_COUNTRY_DROPDOWN_MENU).click()
        self.input_text(self.locators.LOCATOR_COUNTY_INPUT, country)
        self.find_element(self.locators.LOCATOR_US).click()

    def select_state(self):
        select = Select(self.find_element(self.locators.LOCATOR_SELECT_STATES))
        opts = select.options
        state = random.choice(opts)
        select.select_by_value(state.get_attribute('value'))

    def click_logout(self):
        li_logout = self.find_element(self.locators.LOCATOR_LOGOUT)
        li_logout.click()

    def scroll_to_btn_login(self):
        btn_login = self.find_element(self.locators.LOCATOR_BTN_LOGIN)
        self.scroll_to_elem(btn_login)

    def input_login(self, login):
        self.input_text(self.locators.LOCATOR_EMAIL, login)

    def click_login(self):
        btn_login = self.find_element(self.locators.LOCATOR_BTN_LOGIN)
        btn_login.click()

    def tmp(self):
        print(1)
        print(1)
        print(1)
