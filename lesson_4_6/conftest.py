import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login import LoginHelper


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    options.add_argument("no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=900,700")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
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
