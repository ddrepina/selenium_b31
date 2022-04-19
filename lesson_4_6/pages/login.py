from BaseApp import BasePage
from selenium.webdriver.common.by import By


class LoginLocators:
    LOCATOR_UERNAME = (By.NAME, "username")
    LOCATOR_PASSWORD = (By.NAME, "password")
    LOCATOR_LOGIN = (By.NAME, "login")


class LoginHelper(BasePage):
    locators = LoginLocators()

    def enter_username(self):
        login_input = self.find_element(self.locators.LOCATOR_UERNAME)
        login_input.send_keys("admin")

    def enter_password(self):
        login_input = self.find_element(self.locators.LOCATOR_PASSWORD)
        login_input.send_keys("admin")

    def click_login(self):
        self.find_element(self.locators.LOCATOR_LOGIN).click()

    def check_login(self):
        assert "My Store" == self.driver.title, "no My Store"
