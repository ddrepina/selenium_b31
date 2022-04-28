from BaseApp import BasePage
from selenium.webdriver.common.by import By


class AaminCatalogCategoryLocators:
    LOCATOR_TABLE_PRODUCT = (By.CLASS_NAME, 'dataTable')
    LOCATOR_TR = (By.CLASS_NAME, 'row')
    LOCATOR_TD = (By.TAG_NAME, 'td')
    LOCATOR_A = (By.TAG_NAME, 'a')


class AdminCatalogCategoryHelper(BasePage):
    locators = AaminCatalogCategoryLocators()

    def get_link_all_product(self):
        table = self.find_element(self.locators.LOCATOR_TABLE_PRODUCT)
        rows = table.find_elements(*self.locators.LOCATOR_TR)
        # удалить первые три строки. так как там не продукты
        for i in range(3):
            del rows[i]
        link_products = []
        for row in rows:
            tds = row.find_elements(*self.locators.LOCATOR_TD)
            link_products.append(tds[2].find_element(*self.locators.LOCATOR_A).get_attribute('href'))
        return link_products