import time
from pages.PurchaseOfGoods import PurchaseHelper


def test_add_new_product(driver):
    purchase_page = PurchaseHelper(driver)
    for i in range(3):
        purchase_page.go_to_site('en/')
        purchase_page.click_product()
        count_cart = purchase_page.get_count_cart()
        purchase_page.click_add_to_cart()
        purchase_page.wait_upd_cart(count_cart)
    purchase_page.click_checkout()

    elem_product = purchase_page.get_name_product_and_remove_product()
    while elem_product != 'no item':
        purchase_page.check_staleness(elem_product)
        elem_product = purchase_page.get_name_product_and_remove_product()

    # time.sleep(5)
