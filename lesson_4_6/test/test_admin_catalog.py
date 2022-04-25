import time
import random
import os
import pytest
from pages.AdminCatalog import AdminCatalogHelper


@pytest.fixture(scope='function')
def admcatalog_page(driver, auth_admin):
    page = AdminCatalogHelper(driver)
    page.go_to_site('admin/?app=catalog&doc=catalog')
    yield page


def test_add_new_product(driver, admcatalog_page):
    ts = int(time.time())
    name = f'Cat_{ts}'
    print(name)
    quantity = random.randint(10, 30)
    price = random.randint(99, 1000)
    path_to_img = os.getcwd() + f"\\img\\cat_{random.randint(1, 3)}.jpg"
    admcatalog_page.click_add_new_product()
    time.sleep(1)
    admcatalog_page.click_enabled()
    admcatalog_page.input_name(name)
    admcatalog_page.input_code(ts)
    admcatalog_page.click_category()
    admcatalog_page.select_unisex()
    admcatalog_page.input_quantity(quantity)
    admcatalog_page.select_sold_out_status()
    admcatalog_page.input_img(path_to_img)

    admcatalog_page.open_information()
    time.sleep(1)
    admcatalog_page.select_manufacturer()
    admcatalog_page.input_short_desc(f'short description {ts}')
    admcatalog_page.input_desc(f'Text not short description {name}')

    admcatalog_page.open_price()
    time.sleep(1)
    admcatalog_page.input_purchase_price(random.randint(10, 15))
    admcatalog_page.select_purchase_currency()
    admcatalog_page.input_price_usd(price)
    admcatalog_page.input_gross_price_usd(price)
    # time.sleep(15)
    admcatalog_page.click_save()
    time.sleep(2)
    list_product = admcatalog_page.search_name(name)
    assert name in list_product, f'No {name} in list_all_product {list_product}'
