from pages.MainStorePage import MainStorePageHelper


def test_main_store(driver):

    main_store_page = MainStorePageHelper(driver)
    main_store_page.go_to_site('en/')
    main_store_page.check_one_sticker()
