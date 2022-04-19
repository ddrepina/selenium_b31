from pages.MainStorePage import MainStorePageHelper


def test_click_menu(driver):

    admin_page = MainStorePageHelper(driver)
    admin_page.go_to_site('en/')
    admin_page.check_one_sticker()
