from pages.AdminConsole import AdminConsoleHelper


def test_click_menu(driver, auth):

    admin_page = AdminConsoleHelper(driver)
    admin_page.click_all_tabs_main_menu()
