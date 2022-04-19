from BaseApp import BasePage
from selenium.webdriver.common.by import By


class AdminConsoleLocators:
    LOCATOR_MAIN_MENU = (By.ID, "box-apps-menu")
    LOCATOR_LI_APP = (By.ID, "app-")
    LOCATOR_A = (By.TAG_NAME, 'a')
    LOCATOR_LI_NAME = (By.CLASS_NAME, 'name')
    LOCATOR_H1 = (By.TAG_NAME, 'h1')

    LOCATOR_SELECTED_MAIN = (By.CSS_SELECTOR, 'li#app-.selected')
    LOCATOR_SUB_UL = (By.CLASS_NAME, 'docs')
    LOCATOR_LI = (By.TAG_NAME, 'li')


class AdminConsoleHelper(BasePage):
    locators = AdminConsoleLocators()

    def get_lis_main_menu(self):
        all_li_main = self.find_elements(self.locators.LOCATOR_LI_APP)
        all_li = {}
        for main_li_elem in all_li_main:
            main_li_text = main_li_elem.find_element(*self.locators.LOCATOR_LI_NAME).text
            href_main_li = main_li_elem.find_element(*self.locators.LOCATOR_A)
            all_li[main_li_text] = href_main_li.get_attribute('href')
        return all_li

    def get_sub_li(self, min_li):
        all_sub_li = min_li.find_elements(*self.locators.LOCATOR_LI)
        all_li = {}
        for sub_li_elem in all_sub_li:
            main_li_text = sub_li_elem.find_element(*self.locators.LOCATOR_LI_NAME).text
            href_main_li = sub_li_elem.find_element(*self.locators.LOCATOR_A)
            all_li[main_li_text] = href_main_li.get_attribute('href')
        return all_li

    def click_all_tabs_main_menu(self):
        main_lis = self.get_lis_main_menu()
        for main_li in main_lis:
            xpath = f'//ul//a//span[text()="{main_li}"]'
            main_li_elem = self.find_element((By.XPATH, xpath))
            main_li_elem.click()

            # Ждем откртия новой страницы и проверяем наличие заголовка
            h1 = self.find_element(self.locators.LOCATOR_H1).text
            assert h1, f'MAIN TAB. No <h1> in {main_lis[main_li]}'

            # узнаем есть ли подвкладки. если да, то перебираем их
            main_selected = self.find_element(self.locators.LOCATOR_SELECTED_MAIN)
            if len(main_selected.find_elements(*self.locators.LOCATOR_SUB_UL)) > 0:
                all_sub_li = self.get_sub_li(main_selected)
                print(all_sub_li)
                for sub_li in all_sub_li:
                    xpath = f'//ul//a//span[text()="{sub_li}"]'
                    sub_li_elem = self.find_element((By.XPATH, xpath))
                    sub_li_elem.click()
                    h1 = self.find_element(self.locators.LOCATOR_H1).text
                    assert h1, f'sub_li {all_sub_li[sub_li]} '
