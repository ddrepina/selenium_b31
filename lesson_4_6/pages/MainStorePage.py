from BaseApp import BasePage
from selenium.webdriver.common.by import By


class MainStorePageLocators:
    LOCATOR_PRODUCT = (By.CLASS_NAME, 'product')
    LOCATOR_STICKER = (By.CSS_SELECTOR, 'div.sticker')
    LOCATOR_A = (By.TAG_NAME, 'a')
    LOCATOR_PRODUCT_NAME = (By.CLASS_NAME, 'name')


class MainStorePageHelper(BasePage):
    locators = MainStorePageLocators()

    def check_one_sticker(self):
        products = self.find_elements(self.locators.LOCATOR_PRODUCT)
        dict_product = {}
        for product in products:
            product_href = product.find_element(*self.locators.LOCATOR_A).get_attribute('href')
            stickers = product.find_elements(*self.locators.LOCATOR_STICKER)
            assert len(stickers) == 1, f'{product_href} element has {len(stickers)} stickers'
            if product_href in dict_product:
                assert dict_product[product_href]['sticker'][0] == stickers[0].get_attribute('title'), \
                    f'{dict_product[product_href]} ' \
                    f'element has sticker = {dict_product[product_href]["sticker"][0]} ' \
                    f' and ' \
                    f'sticker = {stickers[0].get_attribute("title")}'
            else:
                dict_product[product_href] = {'sticker': [stickers[0].get_attribute('title')]}

        return dict_product
