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
    purchase_page.wait_open_cart()

    purchase_page.remove_product()

    assert purchase_page.cart_is_empty() != 'cart_is_not_empty', 'cart is not empty. see screenshot'

    # time.sleep(5)
