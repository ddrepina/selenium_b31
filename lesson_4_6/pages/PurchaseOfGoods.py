import random

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select

from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PurchaseLocators:
    LOCATOR_PRODUCT = (By.CLASS_NAME, 'product')
    LOCATOR_A = (By.TAG_NAME, 'a')
    LOCATOR_BTN_ADD_TO_CART = (By.NAME, 'add_cart_product')
    LOCATOR_QUANTITY = (By.XPATH, '//span[@class="quantity"]')

    LOCATOR_SIZE = (By.NAME, 'options[Size]')

    LOCATOR_CHECKOUT = (By.XPATH, '//a[contains(text(), "Checkout »")]')
    LOCATOR_CART_PRODUCT = (By.NAME, 'cart_form')
    LOCATOR_NAME_PRODUCT = (By.TAG_NAME, 'strong')
    LOCATOR_SKU = (By.TAG_NAME, 'span')
    LOCATOR_REMOVE = (By.NAME, 'remove_cart_item')

    # LOCATOR_NO_ITEMS = (By.XPATH, '//em[contains(text(), "There are no items in your cart.")]')
    LOCATOR_NO_ITEMS = (By.TAG_NAME, 'em')


class PurchaseHelper(BasePage):
    locators = PurchaseLocators()

    def click_product(self):
        li_product = self.find_element(self.locators.LOCATOR_PRODUCT)
        li_product.find_element(*self.locators.LOCATOR_A).click()

    def get_count_cart(self):
        return int(self.find_element(self.locators.LOCATOR_QUANTITY).text)

    def click_add_to_cart(self):
        wait = WebDriverWait(self.driver, 2)
        try:
            wait.until(EC.visibility_of_element_located(self.locators.LOCATOR_SIZE))
            select = Select(self.find_element(self.locators.LOCATOR_SIZE))
            opts = select.options
            status = random.choice(opts)
            select.select_by_value(status.get_attribute('value'))
            self.find_element(self.locators.LOCATOR_BTN_ADD_TO_CART).click()

        except TimeoutException:
            self.find_element(self.locators.LOCATOR_BTN_ADD_TO_CART).click()

    def wait_upd_cart(self, start_count):
        wait = WebDriverWait(self.driver, 3)
        count = start_count + 1
        wait.until(EC.text_to_be_present_in_element(self.locators.LOCATOR_QUANTITY, str(count)))

    def click_checkout(self):
        self.find_element(self.locators.LOCATOR_CHECKOUT).click()

    def wait_open_cart(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located(self.locators.LOCATOR_CART_PRODUCT))

    def get_name_product_and_remove_product(self):
        wait = WebDriverWait(self.driver, 5)
        # взять имя продукта, чтобы дальше найти его в таблице внизу
        name_product = self.find_element(self.locators.LOCATOR_NAME_PRODUCT).text
        # поиск продукта в таблице Order Summary
        elem = (By.XPATH, f'//td[contains(text(), "{name_product}")]')
        elem_product = self.find_element(elem)
        # удалить продукт
        self.find_element(self.locators.LOCATOR_REMOVE).click()
        try:
            wait.until_not(EC.visibility_of_element_located(self.locators.LOCATOR_NO_ITEMS))
        except TimeoutException:
            return 'no item'
        return elem_product

    def remove_product(self):
        elem_product = self.get_name_product_and_remove_product()
        while elem_product != 'no item':
            self.check_staleness(elem_product)
            elem_product = self.get_name_product_and_remove_product()

    def check_staleness(self, elem_product):
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.staleness_of(elem_product))

    def cart_is_empty(self):
        wait = WebDriverWait(self.driver, 1)
        try:
            wait.until(EC.visibility_of_element_located(self.locators.LOCATOR_NO_ITEMS))
        except:
            self.screenshot('cart_is_not_empty')
            return 'cart_is_not_empty'
