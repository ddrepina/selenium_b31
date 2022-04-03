from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


def test_example(driver):
    driver.get("http://www.google.com/")
    driver.find_element_by_name("q").send_keys("webdriver")
    driver.find_element_by_name("q").send_keys(Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.title_is("webdriver - Поиск в Google"))
    assert driver.find_element_by_id('result-stats'), "no search"