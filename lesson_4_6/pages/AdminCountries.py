from BaseApp import BasePage
from selenium.webdriver.common.by import By


class AdminCountriesLocators:
    LOCATOR_ROW = (By.CLASS_NAME, "row")
    LOCATOR_TD_COUNTRY = (By.TAG_NAME, 'a')
    LOCATOR_TD = (By.TAG_NAME, 'td')

    LOCATOR_TABLE_ZONE = (By.ID, 'table-zones')
    LOCATOR_TR = (By.TAG_NAME, 'tr')
    LOCATOR_INPUT = (By.TAG_NAME, 'input')


class AdminCountriesHelper(BasePage):
    locators = AdminCountriesLocators()

    def check_countries_sort(self):
        rows = self.find_elements(self.locators.LOCATOR_ROW)
        country = []
        for row in rows:
            td_country = row.find_element(*self.locators.LOCATOR_TD_COUNTRY)
            if len(country) > 1:
                if td_country.text.lower() < country[-1].lower():
                    return td_country.text, country[-1]
            country.append(td_country.text)
        return "sort"

    def get_all_countries_name(self):
        rows = self.find_elements(self.locators.LOCATOR_ROW)
        # Собираем все страны в список, так как он сохранит последовательность
        countries = []
        for row in rows:
            td_country = row.find_element(*self.locators.LOCATOR_TD_COUNTRY)
            countries.append(td_country.text)
        return countries

    def get_all_countries_with_zone(self):
        rows = self.find_elements(self.locators.LOCATOR_ROW)
        countries_zone = {}
        # в данном случае нам уже не важен порядок стран на странице, поэтому
        # создаем словарь вида {Название страны: ссылка на страницу страны}
        for row in rows:
            td_country = row.find_element(*self.locators.LOCATOR_TD_COUNTRY)
            tds = row.find_elements(*self.locators.LOCATOR_TD)
            if tds[5].text != '0':
                countries_zone[td_country.text] = td_country.get_attribute('href')
        return countries_zone

    def get_all_zone(self):
        table_zone = self.find_element(self.locators.LOCATOR_TABLE_ZONE)
        rows = table_zone.find_elements(*self.locators.LOCATOR_TR)
        # удаляем первую строку, потому что в ней шапка таблицы
        rows.pop(0)
        rows.pop(-1)
        all_zone = []
        for row in rows:
            tds = row.find_elements(*self.locators.LOCATOR_TD)
            name = tds[2].text
            all_zone.append(name)
        return all_zone

    def check_sort_zone(self):
        all_countries_with_zone = self.get_all_countries_with_zone()
        for country_with_zone in all_countries_with_zone:
            # открываем страницу страны
            self.go_to_link(all_countries_with_zone[country_with_zone])
            # берем все зоны
            all_zone = self.get_all_zone()
            is_sort = self.is_sorted(all_zone)
            if is_sort != True:
                is_sort.append(country_with_zone)
                is_sort.append(all_countries_with_zone[country_with_zone])
                return is_sort
            else:
                return True
