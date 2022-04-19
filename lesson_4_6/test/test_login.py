from pages.login import LoginHelper


def test_login(driver):
    login_page = LoginHelper(driver)
    login_page.go_to_site("admin/")
    login_page.enter_username()
    login_page.enter_password()
    login_page.click_login()
    login_page.check_login()
