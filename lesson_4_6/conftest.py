import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login import LoginHelper
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(by, value)

    def after_find(self, by, value, driver):
        print(by, value, "found")

    def on_exception(self, exception, driver):
        print(exception)


@pytest.fixture(scope="session")
def driver_listener():
    options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    options.add_argument("no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=900,700")
    options.add_argument("--disable-dev-shm-usage")
    driver = EventFiringWebDriver(webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options))
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def driver_с():
    options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    options.add_argument("no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=900,700")
    options.add_argument("--disable-dev-shm-usage")

    caps = DesiredCapabilities().CHROME
    caps['goog:loggingPrefs'] = {'performance': 'ALL', 'driver': 'ALL', 'browser': 'ALL'}

    driver = webdriver.Chrome(ChromeDriverManager().install(),
                              chrome_options=options,
                              desired_capabilities=caps)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def driver():
    options = webdriver.FirefoxOptions()
    # options.add_argument("headless")
    options.add_argument("no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=900,700")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                               options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def auth_admin(driver):
    login_page = LoginHelper(driver)
    login_page.go_to_site("admin/")
    login_page.enter_username()
    login_page.enter_password()
    login_page.click_login()
    WebDriverWait(driver, 10).until(EC.title_is("My Store"))
