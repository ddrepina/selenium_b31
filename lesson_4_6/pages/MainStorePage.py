from BaseApp import BasePage
from selenium.webdriver.common.by import By


class MainStorePageLocators:
    LOCATOR_PRODUCT = (By.CLASS_NAME, 'product')
    LOCATOR_STICKER = (By.CSS_SELECTOR, 'div.sticker')
    LOCATOR_A = (By.TAG_NAME, 'a')
    LOCATOR_PRODUCT_NAME = (By.CLASS_NAME, 'name')

    LOCATOR_BOX_CAMPAIGNS = (By.ID, 'box-campaigns')
    # заголовок campaigns
    LOCATOR_H3 = (By.TAG_NAME, 'h3')
    LOCATOR_PRODUCT_REGULAR_PRICE = (By.CLASS_NAME, 'regular-price')
    LOCATOR_PRODUCT_CAMPAIGN_PRICE = (By.CLASS_NAME, 'campaign-price')

    LOCATOR_PP_PRODUCT_BOX = (By.ID, 'box-product')
    LOCATOR_PP_PRODUCT_NAME = (By.TAG_NAME, 'h1')


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

    def scroll_to_campaigns(self):
        box = self.find_element(self.locators.LOCATOR_BOX_CAMPAIGNS)
        campaign_title = box.find_element(*self.locators.LOCATOR_H3)
        self.scroll_to_elem(campaign_title)

    def get_product_name(self):
        campaigns = self.find_element(self.locators.LOCATOR_BOX_CAMPAIGNS)
        return campaigns.find_element(*self.locators.LOCATOR_PRODUCT_NAME).text

    def get_product_href(self):
        campaigns = self.find_element(self.locators.LOCATOR_BOX_CAMPAIGNS)
        return campaigns.find_element(*self.locators.LOCATOR_A).get_attribute('href')

    def get_regular_price_and_values_css(self):
        campaigns = self.find_element(self.locators.LOCATOR_BOX_CAMPAIGNS)
        elem = campaigns.find_element(*self.locators.LOCATOR_PRODUCT_REGULAR_PRICE)
        regular_price_and_value = {'regular_price': elem.text}
        types_css = ['color', 'font-weight', 'font-size', 'text-decoration']
        regular_price_and_value.update(self.value_of_css(elem, types_css))
        return regular_price_and_value

    def get_campaign_price_and_values_css(self):
        campaigns = self.find_element(self.locators.LOCATOR_BOX_CAMPAIGNS)
        elem = campaigns.find_element(*self.locators.LOCATOR_PRODUCT_CAMPAIGN_PRICE)
        campaign_price_and_value = {'campaign_price': elem.text}
        types_css = ['color', 'font-weight', 'font-size', 'text-decoration']
        campaign_price_and_value.update(self.value_of_css(elem, types_css))
        return campaign_price_and_value

    def check_grey(self, color):
        return all([color[0] == color[1], color[1] == color[2]])

    def check_red(self, color):
        return all([color[1] == 0, color[2] == 0])

    def check_line_through(self, line):
        return 'line-through' in line

    def check_campaign_size_big_regular_size(self, campaign_size, regular_size):
        return campaign_size > regular_size

    def check_campaign_weight_big_regular_wight(self, campaign_weight, regular_weight):
        return campaign_weight > regular_weight

    def get_pp_product_name(self):
        campaigns = self.find_element(self.locators.LOCATOR_PP_PRODUCT_BOX)
        return campaigns.find_element(*self.locators.LOCATOR_PP_PRODUCT_NAME).text

    def get_pp_regular_price_and_values_css(self):
        elem = self.find_element(self.locators.LOCATOR_PRODUCT_REGULAR_PRICE)
        regular_price_and_value = {'regular_price': elem.text}
        types_css = ['color', 'font-weight', 'font-size', 'text-decoration']
        regular_price_and_value.update(self.value_of_css(elem, types_css))
        return regular_price_and_value

    def get_pp_campaign_price_and_values_css(self):
        elem = self.find_element(self.locators.LOCATOR_PRODUCT_CAMPAIGN_PRICE)
        regular_price_and_value = {'campaign_price': elem.text}
        types_css = ['color', 'font-weight', 'font-size', 'text-decoration']
        regular_price_and_value.update(self.value_of_css(elem, types_css))
        return regular_price_and_value
