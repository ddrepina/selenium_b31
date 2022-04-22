from BaseApp import BasePage
from selenium.webdriver.common.by import By


class AdminGeoZoneLocators:
    LOCATOR_ROW = (By.CLASS_NAME, "row")
    LOCATOR_TD_COUNTRY = (By.TAG_NAME, 'a')

    LOCATOR_TABLE_ZONE = (By.ID, 'table-zones')
    LOCATOR_TR = (By.TAG_NAME, 'tr')
    LOCATOR_TD = (By.TAG_NAME, 'td')

    LOCATOR_SELECTED = (By.CSS_SELECTOR, '[selected="selected"]')


class AdminGeoZoneHelper(BasePage):
    locators = AdminGeoZoneLocators()

    def get_all_countries(self):
        rows = self.find_elements(self.locators.LOCATOR_ROW)
        countries = {}
        for row in rows:
            name_countries = row.find_element(*self.locators.LOCATOR_TD_COUNTRY)
            countries[name_countries.text] = name_countries.get_attribute('href')
        return countries

    def check_sort_geozone(self, all_countries):
        all_countries = self.get_all_countries()
        for country in all_countries:
            self.go_to_link(all_countries[country])
            table_zone = self.find_element(self.locators.LOCATOR_TABLE_ZONE)
            rows = table_zone.find_elements(*self.locators.LOCATOR_TR)
            rows.pop(0)
            rows.pop(-1)
            zones = []
            for row in rows:
                tds = row.find_elements(*self.locators.LOCATOR_TD)
                name = tds[2].find_element(*self.locators.LOCATOR_SELECTED).text
                if len(zones) > 1:
                    if name.lower() < zones[-1].lower():
                        return name, zones[-1]
                zones.append(name)
        return "sort"
