from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import random


class AaminCatalogLocators:
    LOCATOR_ADD_NEW_PRODUCT = (By.XPATH, '//a[contains(text(), " Add New Product")]')
    LOCATOR_ENABLED_LABEL = (By.XPATH, '//label[contains(text(), " Enabled")]')
    LOCATOR_ENABLED_RADIOBTN = (By.CSS_SELECTOR, 'input[value="1"]')
    LOCATOR_NAME = (By.NAME, 'name[en]')
    LOCATOR_CODE = (By.NAME, 'code')
    LOCATOR_SUBCATEGORY = (By.CSS_SELECTOR, '[data-name="Subcategory"]')
    LOCATOR_GENDER = (By.NAME, 'product_groups[]')
    LOCATOR_QUANTITY = (By.NAME, 'quantity')
    LOCATOR_SELECT_SOLD_OUT_STATUS = (By.NAME, 'sold_out_status_id')
    LOCATOR_INPUT_IMG = (By.NAME, 'new_images[]')

    LOCATOR_TABS = (By.CLASS_NAME, 'tabs')

    LOCATOR_TAB_INFO = (By.XPATH, '//li/a[contains(text(), "Information")]')
    LOCATOR_MANUFACTURER = (By.NAME, 'manufacturer_id')
    LOCATOR_SHORT_DESC = (By.NAME, 'short_description[en]')
    LOCATOR_DESC = (By.CLASS_NAME, 'trumbowyg-editor')

    LOCATOR_TAB_PRICE = (By.XPATH, '//li/a[contains(text(), "Prices")]')
    LOCATOR_PURCHASE_PRICE = (By.NAME, 'purchase_price')
    LOCATOR_PURCHASE_CURRENCY = (By.NAME, 'purchase_price_currency_code')
    LOCATOR_PRICE_USD = (By.NAME, 'prices[USD]')
    LOCATOR_GROSS_PRICE_USD = (By.NAME, 'gross_prices[USD]')

    LOCATOR_SAVE = (By.NAME, 'save')

    LOCATOR_TABLE_PRODUCT = (By.CLASS_NAME, 'dataTable')
    LOCATOR_TR = (By.CLASS_NAME, 'row')
    LOCATOR_TD = (By.TAG_NAME, 'td')
    LOCATOR_A = (By.TAG_NAME, 'a')

    LOCATOR_SEARCH = (By.NAME, 'query')


class AdminCatalogHelper(BasePage):
    locators = AaminCatalogLocators()

    def click_add_new_product(self):
        self.find_element(self.locators.LOCATOR_ADD_NEW_PRODUCT).click()

    def click_enabled(self):
        label = self.find_element(self.locators.LOCATOR_ENABLED_LABEL)
        label.find_element(*self.locators.LOCATOR_ENABLED_RADIOBTN).click()

    def input_name(self, name):
        self.input_text(self.locators.LOCATOR_NAME, name)

    def input_code(self, code):
        self.input_text(self.locators.LOCATOR_CODE, code)

    def click_category(self):
        self.find_element(self.locators.LOCATOR_SUBCATEGORY).click()

    def select_unisex(self):
        genders = self.find_elements(self.locators.LOCATOR_GENDER)
        genders[2].click()

    def input_quantity(self, quantity):
        self.input_text(self.locators.LOCATOR_QUANTITY, quantity)

    def select_sold_out_status(self):
        select = Select(self.find_element(self.locators.LOCATOR_SELECT_SOLD_OUT_STATUS))
        opts = select.options
        status = random.choice(opts)
        select.select_by_value(status.get_attribute('value'))

    def input_img(self, path_to_img):
        self.find_element(self.locators.LOCATOR_INPUT_IMG).send_keys(path_to_img)

    def open_information(self):
        tabs = self.find_element(self.locators.LOCATOR_TABS)
        info = tabs.find_element(*self.locators.LOCATOR_TAB_INFO)
        self.scroll_to_elem(info)
        info.click()

    def select_manufacturer(self):
        select = Select(self.find_element(self.locators.LOCATOR_MANUFACTURER))
        select.select_by_visible_text('ACME Corp.')

    def input_short_desc(self, text):
        self.input_text(self.locators.LOCATOR_SHORT_DESC, text)

    def input_desc(self, text):
        self.input_text(self.locators.LOCATOR_DESC, text)

    def open_price(self):
        tabs = self.find_element(self.locators.LOCATOR_TABS)
        price = tabs.find_element(*self.locators.LOCATOR_TAB_PRICE)
        self.scroll_to_elem(price)
        price.click()

    def input_purchase_price(self, pprice):
        self.input_text(self.locators.LOCATOR_PURCHASE_PRICE, pprice)

    def select_purchase_currency(self):
        select = Select(self.find_element(self.locators.LOCATOR_PURCHASE_CURRENCY))
        opts = select.options
        currency = random.choice(opts)
        select.select_by_value(currency.get_attribute('value'))

    def input_price_usd(self, text):
        self.input_text(self.locators.LOCATOR_PRICE_USD, text)

    def input_gross_price_usd(self, text):
        self.input_text(self.locators.LOCATOR_GROSS_PRICE_USD, text)

    def click_save(self):
        self.find_element(self.locators.LOCATOR_SAVE).click()

    def search_name(self, name):
        input_elem = self.find_element(self.locators.LOCATOR_SEARCH)
        input_elem.clear()
        input_elem.send_keys(name)
        input_elem.send_keys(Keys.ENTER)
        table = self.find_element(self.locators.LOCATOR_TABLE_PRODUCT)
        rows = table.find_elements(*self.locators.LOCATOR_TR)
        name_products = []
        for row in rows:
            tds = row.find_elements(*self.locators.LOCATOR_TD)
            name_products.append(tds[2].find_element(*self.locators.LOCATOR_A).text)
        return name_products
